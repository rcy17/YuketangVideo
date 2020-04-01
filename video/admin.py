from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_code', 'status', 'add_time', 'finish_time')
    list_display_links = list_display
    readonly_fields = ('file', 'room_code', 'status')

