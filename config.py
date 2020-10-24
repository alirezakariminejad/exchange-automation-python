BASE_PATH = "http://data.fixer.io/api/latest?access_key="
API_KEY = "74186fd800b83056bf66acc1901a7218"

url = BASE_PATH + API_KEY

receiver_mail = "alireza.kariminejad@yahoo.com"

rules = {
    "archive": True,
    "send_mail": True,
    "preferred_rates": ["AED", "IRR", "USD", "BTN"]
}
