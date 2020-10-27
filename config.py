BASE_PATH = "http://data.fixer.io/api/latest?access_key="
API_KEY = "74186fd800b83056bf66acc1901a7218"

url = BASE_PATH + API_KEY

rules = {
    "archive": True,
    "mail": {
        "enable": True,
        "receiver_mail": "alireza.kariminejad@yahoo.com",
        "preferred_rates": ["AED", "IRR", "USD", "BTN"]
    },
    "sms": {
        "enable": True,
        "receiver_mail": "09123655055",
        "preferred_rates": {
            "IRR": {"min": 80.059998, "max": 85.059990},
            "BTN": {"min": 49782, "max": 50000}
        }
    },
}
