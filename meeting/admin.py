from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Meeting

# admin.site.register(Meeting, SimpleHistoryAdmin)


@admin.register(Meeting)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "coach",
        "student",
        "created_time",
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

        if "audio_file" in form.changed_data and obj.audio_file:
            obj.fetch_content()
