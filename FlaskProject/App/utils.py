# 其他函数
import hashlib
import time
import requests

def send_verify_code(mobile):
    url = "https://api.netease.im/sms/sendcode.action"
    appkey = "58fab429641d3b1ce9e2e00ede008fbc"
    appsecret = "e94ee1d83d2d"
    nonce = hashlib.new("sha512", str(time.time()).encode("utf-8")).hexdigest()
    curtime = str(int(time.time()))
    checksum = hashlib.new("sha1", (appsecret+nonce+curtime).encode("utf-8")).hexdigest()

    headers = {
        "AppKey": appkey,
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": checksum
    }

    form_data = {
        "mobile":mobile,
    }

    resp = requests.post(url, data=form_data, headers=headers)
    return resp