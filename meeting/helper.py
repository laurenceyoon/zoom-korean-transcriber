import requests
from django.conf import settings


def get_transcription_clova_api(audio_data=None, audio_path=None):
    lang = "Kor"  # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = audio_data or open(audio_path, "rb")
    headers = {
        "X-NCP-APIGW-API-KEY-ID": settings.CLOVA_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": settings.CLOVA_CLIENT_SECRET,
        "Content-Type": "application/octet-stream",
    }
    print("Requesting transcription to CLOVA...")
    response = requests.post(url, data=data, headers=headers)
    print(f"response from CLOVA: {response}, OK? {response.ok}")
    if response.ok:
        print("Fetching transribed text Done.")
        return response.json()["text"]
    else:
        return response.text


def get_transcription_kakao_api(audio_path):
    url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "Transfer-Encoding": "chunked",
        "Authorization": "KakaoAK " + settings.KAKAO_REST_API_KEY,
    }

    with open(audio_path, "rb") as f:
        audio = f.read()

    response = requests.post(url, headers=headers, data=audio)
    return response.text


def get_last_transcription_text(meeting_id):
    if not meeting_id:
        meeting_id = settings.ZOOM_MEETING_ID
    print(f"Getting last transcription text for Meeting ID({meeting_id})...")
    audio_data = get_last_recording_from_zoom(meeting_id)
    transcription_text = get_transcription_clova_api(audio_data=audio_data)
    return transcription_text


def get_last_recording_from_zoom(meeting_id):
    url = f"https://api.zoom.us/v2/meetings/{meeting_id}/recordings"

    payload = {}
    headers = {"Authorization": f"Bearer {settings.ZOOM_JWT_TOKEN}"}
    print(f"Fetching Audio File from Zoom...")
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.ok:
        response = response.json()
        download_url = next(
            file["download_url"]
            for file in response["recording_files"]
            if file["recording_type"] == "audio_only"
        )
        print(f"download_url: {download_url}")

        audio_response = requests.get(download_url)
        print("Downloading Audio File Done.")
        audio_data = audio_response.content
        return audio_data
