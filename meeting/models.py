from django.db import models
from django.utils import timezone
from django.conf import settings
import os
from simple_history.models import HistoricalRecords

from .helper import test_clova_api


class Meeting(models.Model):
    coach = models.CharField(max_length=50, blank=True)
    student = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=256, blank=True)
    meeting_id = models.CharField(max_length=256, blank=True)

    audio_file = models.FileField(blank=True)
    content = models.TextField(blank=True)

    created_time = models.DateTimeField(default=timezone.now)
    ended_time = models.DateTimeField(null=True, blank=True)

    history = HistoricalRecords()

    def fetch_content(self):
        path = os.path.join(settings.MEDIA_ROOT, str(self.audio_file))
        result = test_clova_api(path)
        print(f"result: {result}")
        self.content = result["text"]
        self.save()
