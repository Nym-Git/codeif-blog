# Generated by Django 3.2.6 on 2021-08-26 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0011_auto_20210826_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
