import os
from pathlib import Path
from threading import Timer

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from .models import Video


def _download(instance: Video):
    Video.objects.filter(pk=instance.pk).update(status=Video.VideoStatus.DOWNLOADING)
    filename = f'{instance.room_code}.mp4'
    parent = Path(settings.MEDIA_ROOT)
    parent.mkdir(exist_ok=True)
    path = parent.joinpath(filename)
    log = parent.joinpath(f'{instance.room_code}.log')
    cmd = f'ffmpeg -y -i {instance.url} {path} > {log} 2>&1'
    error = os.system(cmd)
    instance = Video.objects.get(pk=instance.pk)
    if error:
        instance.status = Video.VideoStatus.ERROR
    else:
        instance.status = Video.VideoStatus.FINISHED
        instance.file.name = filename
    instance.save()


@receiver(post_save, sender=Video)
def download(sender, instance: Video, created, **kwargs):
    if created:
        Timer(2, _download, [instance]).start()
