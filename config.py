from localConfig import PHONE_NUM
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
        "receiver_sms": PHONE_NUM,
        "preferred_rates": {
            "IRR": {"min": 48800.407586, "max": 50800.407586},
            "BTN": {"min": 85.090735, "max": 84.090735}
        }
    },
}
