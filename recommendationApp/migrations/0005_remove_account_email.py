# Generated by Django 5.0.6 on 2024-05-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0004_video_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
    ]
