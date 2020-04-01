# Generated by Django 3.0.3 on 2020-04-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Waiting'), (1, 'Downloading'), (2, 'Error'), (3, 'Finished')], default=0)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('room_code', models.CharField(blank=True, max_length=32, null=True, unique=True)),
            ],
        ),
    ]
