import requests
import json
from config import url, rules


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def archive(filename, rates):
    with open(f'Archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    subject = f"{timestamp} rates"
    temp_exc = dict()
    if rules["preferred_rates"] is not None:
        for exch in rules["preferred_rates"]:
            temp_exc[exch] = rates[exch]
    rates = temp_exc
    text = rates


if __name__ == "__main__":
    res = get_rates()
    if rules["archiver"]:
        archive(res["timestamp"], res["rates"])
    if rules["send_mail"]:
        send_mail(res["timestamp"], res["rates"])
