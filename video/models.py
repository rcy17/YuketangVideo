

from django.db import models
from django.core.exceptions import ValidationError


class Video(models.Model):
    class VideoStatus(models.IntegerChoices):
        WAITING = 0
        DOWNLOADING = 1
        ERROR = 2
        FINISHED = 3

    name = models.CharField(max_length=32, null=True, blank=True)
    url = models.URLField()
    add_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=VideoStatus.choices, default=VideoStatus.WAITING)
    file = models.FileField(null=True, blank=True)
    room_code = models.CharField(unique=True, null=True, blank=True, max_length=32)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            try:
                self.room_code = self.url.split('/')[-2]
            except:
                raise ValidationError('url有误')
            if not self.name:
                self.name = self.room_code
        return super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return super().delete(using, keep_parents)
