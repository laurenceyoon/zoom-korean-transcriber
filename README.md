# Zoom Korean Transcriber

A simple django application for audio transcription from recorded Zoom Meeting, via [Clova Speech Recognition API](https://api.ncloud-docs.com/docs/ai-naver-clovaspeechrecognition-stt).

This app only provides admin site for managing Korean transcription from recorded Zoom Meeting.

- Version information:
    - python >= 3.8.x
    - SQLite3
    - Django 3.x

How to install:

```bash
$ pyenv shell 3.8.x
$ git clone git@github.com:laurenceyoon/django-with-clova-csr.git
$ cd django-with-clova-csr
$ pip install -r requirements.txt
```

You'll need to configure the environment variable listed below and save to `.env` file:

```bash
DJANGO_SECRET_KEY
CLOVA_CLIENT_ID
CLOVA_CLIENT_SECRET
ZOOM_JWT_TOKEN
```

For the credentials of [Naver Cloud Platform](https://www.ncloud.com/) and [Zoom](https://developers.zoom.us/), please refer to the each link.

To add a new admin account, execute below and enter the account information:
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

Run django application and go to `127.0.0.1:8000/admin`:

```bash
$ python manage.py runserver
```
