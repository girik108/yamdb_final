# Generated by Django 3.1 on 2020-11-29 02:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20201117_1107'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0006_comments_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
