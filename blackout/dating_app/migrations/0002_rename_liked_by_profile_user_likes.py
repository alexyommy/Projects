# Generated by Django 3.2.4 on 2021-06-20 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='liked_by',
            new_name='user_likes',
        ),
    ]