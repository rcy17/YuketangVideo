from uuid import uuid4

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User


class Command(BaseCommand):
    help = 'Initialize some settings in database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        password = uuid4().hex
        username = 'admin'
        User.objects.create_superuser(
            username=username,
            password=password,
        )
        group = Group.objects.create(name='downloader')
        group.permissions.set(Permission.objects.filter(codename__in=['view_video', 'add_video', 'delete_video']))
        self.stdout.write(password)


