# Generated by Django 3.0.7 on 2020-06-18 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outset', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='following_count',
            new_name='followings_count',
        ),
    ]