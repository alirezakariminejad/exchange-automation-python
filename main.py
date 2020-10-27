import requests
import json
from mail import send_msg_smtp
from config import url, rules
from sms import send_sms


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
    if ["preferred_rates"] is not None:
        for exch in rules["mail"]["preferred_rates"]:
            temp_exc[exch] = rates[exch]
    rates = temp_exc
    text = json.dumps(rates)
    send_msg_smtp(subject, text)


def can_i_send_sms(rates):
    msg = ""
    for exch in rules["sms"]["preferred_rates"]:
        if rates[exch] <= rules["sms"]["preferred_rates"][exch]["min"]:
            msg += f'{exch} reached min {rates[exch]} \n'
        if rates[exch] >= rules["sms"]["preferred_rates"][exch]["max"]:
            msg += f'{exch} reached max {rates[exch]} \n'
    return msg


if __name__ == "__main__":
    res = get_rates()
    if rules["archive"]:
        archive(res["timestamp"], res["rates"])
    if rules["mail"]["enable"]:
        send_mail(res["timestamp"], res["rates"])
    if rules["sms"]["enable"]:
        msg_sms = can_i_send_sms(res["rates"])
        print(msg_sms)
        if msg_sms:
            send_sms(msg_sms)
