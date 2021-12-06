import sys
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

CLOVA_CLIENT_ID = os.getenv("CLOVA_CLIENT_ID")
CLOVA_CLIENT_SECRET = os.getenv("CLOVA_CLIENT_SECRET")
KAKAO_REST_API_KEY = os.getenv("KAKAO_REST_API_KEY")


def test_clova_api(audio_path):
    lang = "Kor"  # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = open(audio_path, "rb")
    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLOVA_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": CLOVA_CLIENT_SECRET,
        "Content-Type": "application/octet-stream",
    }

    response = requests.post(url, data=data, headers=headers)
    print(f"response: {response}, OK? {response.ok}")
    if response.ok:
        return response.json()
    else:
        return response.text


def test_kakao_api(audio_path):
    url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "Transfer-Encoding": "chunked",
        "Authorization": "KakaoAK " + KAKAO_REST_API_KEY,
    }

    with open(audio_path, "rb") as f:
        audio = f.read()

    response = requests.post(url, headers=headers, data=audio)
    print(response.text)
