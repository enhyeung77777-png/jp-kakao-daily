import os
import json
import requests
from datetime import datetime

def build_message():
    jp = "きょうは あめが ふっています"
    pron = "쿄오와 아메가 후잇테이마스"
    ko = "오늘은 비가 오고 있어"

    message = f"[오늘의 일본어]\n\n{jp}\n{pron}\n{ko}\n\n"
    message += "■ 단어\n"
    message += "きょう - 쿄오 - 오늘\n"
    message += "あめ - 아메 - 비\n"
    message += "ふる - 후루 - 내리다\n\n"
    message += "■ 문법\n"
    message += "〜ている - 진행형 (~하고 있다)\n"
    return message

def send_to_me(text, token):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    body = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": text
        }, ensure_ascii=False)
    }
    return requests.post(url, headers=headers, data=body)

def main():
    token = os.environ.get("KAKAO_ACCESS_TOKEN")
    msg = build_message()
    send_to_me(msg, token)
