# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "fsm"
app_title = "Erpnext Field Service Sla Dispatcher"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Field Service Sla Dispatcher - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/fsm/css/fsm.bundle.css"
app_include_js = "/assets/fsm/js/fsm.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Field Service Sla Dispatcher Entry": {
        "validate": "fsm.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "fsm.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "fsm.tasks.hourly_sync"
    ],
    "daily": [
        "fsm.tasks.daily_reconciliation"
    ],
    "weekly": [
        "fsm.tasks.weekly_digest"
    ]
}
