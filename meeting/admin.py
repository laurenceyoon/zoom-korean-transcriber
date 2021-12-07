from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .helper import get_last_transcription_text
from .models import Meeting


@admin.register(Meeting)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "coach",
        "student",
        "created_time",
        "is_content",
        "fetch",
    )
    list_per_page = 20

    def is_content(self, obj):
        return obj.content != ""

    is_content.boolean = True
    is_content.short_description = "업데이트 여부"

    def fetch(self, obj):
        path = reverse("admin:meeting_meeting_change", args=[obj.pk]) + "?fetch=True"
        return format_html(f'<a class="button" href="{path}">받아오기</a>')

    fetch.short_description = "새로 가져오기"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        is_fetch_triggered = request.GET.get("fetch", False)
        if object_id is not None and is_fetch_triggered:
            obj = Meeting.objects.get(pk=object_id)
            transcription_text = get_last_transcription_text(meeting_id=obj.meeting_id)
            obj.content = transcription_text
            obj.save()

        return super().change_view(
            request, object_id, form_url=form_url, extra_context=extra_context
        )
