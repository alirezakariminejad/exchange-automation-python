from kavenegar import *
from localConfig import SMS_API_Key
from config import rules


def send_sms(msg):
    try:
        api = KavenegarAPI(SMS_API_Key)
        params = {
            'sender': '1000596446',
            'receptor': rules["sms"]["receiver_sms"],
            'message': msg
        }
        response = api.sms_send(params)
        print(str(response))
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
