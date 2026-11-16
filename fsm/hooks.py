# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "fsm"
app_title = "Erpnext Field Service Sla Dispatcher"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Field Service Sla Dispatcher for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/fsm/css/fsm.bundle.css"
app_include_js = "/assets/fsm/js/fsm.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "fsm.engine.on_document_submit",
        "on_cancel": "fsm.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "fsm.engine.daily_scheduled_sync"
    ]
}
