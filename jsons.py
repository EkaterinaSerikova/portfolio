"""
BACKOFFICE DASHBOARDS
"""
HISTORY = {
    "at": None,
    "description": None,
    "eventType": None,
    "id": None,
    "ip": None,
    "user": {
        "id": None,
        "email": f"{settings.RANDOM_STRING}",
        "fullName": None}
}

"""
ADMIN PAYMENT SYSTEM
"""
CREATE_PAYMENT_SYSTEM = {
    "title": None,
    "ps_fields": {
        "type": "Manual",
        "value": {
            "currencies": ["USD", "EUR", "JPY"],
            "deposit_commission": {
                "fixed": {
                    "amount": 0,
                    "currency": "USD"
                },
                "percent": 0,
                "min": 0,
                "max": 10000
            },
            "withdraw_commission": {
                "fixed": {
                    "amount": 0,
                    "currency": "USD"
                },
                "percent": 0,
                "min": 0,
                "max": 1000
            },
            "invoice": {
                "type": "disabled",
                "value": {
                    "null": ""
                }
            },
            "payment_proof": True
        }
    }
}
