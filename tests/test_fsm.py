import unittest
from fsm.engine import FieldServiceDispatcherEngine, ServiceTechnician, CustomerServiceTicket

class TestFieldServiceDispatch(unittest.TestCase):
    def test_nearest_technician_dispatch_with_van_stock(self):
        engine = FieldServiceDispatcherEngine()

        t1 = ServiceTechnician(
            tech_id="TECH-01",
            tech_name="Amit Sharma",
            latitude=19.0760, # Mumbai
            longitude=72.8777,
            certified_skills=["ELEVATOR_HYDRAULICS", "ELECTRICAL"],
            van_stock_inventory={"VALVE-HYD-50": 2, "FUSE-10A": 10}
        )
        t2 = ServiceTechnician(
            tech_id="TECH-02",
            tech_name="Vikram Rao",
            latitude=19.1200, # Further away in Andheri
            longitude=72.8500,
            certified_skills=["ELEVATOR_HYDRAULICS"],
            van_stock_inventory={"VALVE-HYD-50": 1}
        )

        ticket = CustomerServiceTicket(
            ticket_id="TKT-ELEV-99",
            customer_name="Grand Hyatt Mumbai",
            latitude=19.0800,
            longitude=72.8700,
            required_skill="ELEVATOR_HYDRAULICS",
            required_spare_parts={"VALVE-HYD-50": 1}
        )

        res = engine.dispatch_nearest_technician(ticket, [t1, t2])
        self.assertEqual(res.status, "DISPATCHED")
        self.assertEqual(res.assigned_tech_id, "TECH-01")
        self.assertLess(res.distance_km, 5.0)
        # Tech 1 van stock reduced from 2 to 1
        self.assertEqual(t1.van_stock_inventory["VALVE-HYD-50"], 1)

if __name__ == "__main__":
    unittest.main()
