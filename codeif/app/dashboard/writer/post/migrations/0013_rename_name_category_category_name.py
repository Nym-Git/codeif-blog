# Generated by Django 3.2.6 on 2021-08-26 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='Category_name',
        ),
    ]
