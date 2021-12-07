# Zoom Korean Transcriber

A simple django application for audio transcription via Clova Speech Recognition API.

This app only provides admin site for retrieving Korean transcription from recorded Zoom Meeting and save the text into the meeting table in local database.

- Version settings:
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


Run django application and go to `127.0.0.1:8000/admin`:

```
$ python manage.py runserver
```
