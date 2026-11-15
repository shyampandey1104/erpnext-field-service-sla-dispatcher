"""Field Service Management (FSM) Geolocation Technician Dispatch & Van-Stock Spare Parts Engine."""

import math
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ServiceTechnician:
    tech_id: str
    tech_name: str
    latitude: float
    longitude: float
    certified_skills: List[str]
    van_stock_inventory: Dict[str, int]  # item_code -> quantity
    is_available: bool = True


@dataclass
class CustomerServiceTicket:
    ticket_id: str
    customer_name: str
    latitude: float
    longitude: float
    required_skill: str
    required_spare_parts: Dict[str, int]
    sla_max_response_hours: float = 4.0


@dataclass
class DispatchAssignmentResult:
    ticket_id: str
    assigned_tech_id: str
    assigned_tech_name: str
    distance_km: float
    has_all_required_spare_parts: bool
    status: str  # DISPATCHED, REJECTED_NO_SKILLED_TECH_AVAILABLE, REJECTED_PARTS_UNAVAILABLE


class FieldServiceDispatcherEngine:
    """Matches breakdown tickets with the nearest certified technician carrying needed van-stock spares."""

    def calculate_haversine_distance_km(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        # Earth radius in kilometers
        R = 6371.0
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 2)

    def dispatch_nearest_technician(
        self,
        ticket: CustomerServiceTicket,
        technicians: List[ServiceTechnician]
    ) -> DispatchAssignmentResult:
        qualified_candidates = []

        for tech in technicians:
            if not tech.is_available:
                continue
            if ticket.required_skill not in tech.certified_skills:
                continue

            # Check van-stock spare parts
            has_parts = True
            for part_code, qty_needed in ticket.required_spare_parts.items():
                if tech.van_stock_inventory.get(part_code, 0) < qty_needed:
                    has_parts = False
                    break

            if has_parts:
                dist = self.calculate_haversine_distance_km(
                    lat1=ticket.latitude,
                    lon1=ticket.longitude,
                    lat2=tech.latitude,
                    lon2=tech.longitude
                )
                qualified_candidates.append((dist, tech))

        if not qualified_candidates:
            return DispatchAssignmentResult(
                ticket_id=ticket.ticket_id,
                assigned_tech_id="NONE",
                assigned_tech_name="NONE",
                distance_km=0.0,
                has_all_required_spare_parts=False,
                status="REJECTED_NO_SUITABLE_TECH_AVAILABLE"
            )

        # Sort by shortest distance
        qualified_candidates.sort(key=lambda x: x[0])
        best_distance, best_tech = qualified_candidates[0]

        # Deduct van stock
        for part_code, qty_needed in ticket.required_spare_parts.items():
            best_tech.van_stock_inventory[part_code] -= qty_needed
        best_tech.is_available = False

        return DispatchAssignmentResult(
            ticket_id=ticket.ticket_id,
            assigned_tech_id=best_tech.tech_id,
            assigned_tech_name=best_tech.tech_name,
            distance_km=best_distance,
            has_all_required_spare_parts=True,
            status="DISPATCHED"
        )
