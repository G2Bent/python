# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170829_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='fileway',
            field=models.FileField(upload_to='web/hey/Heygears/Excel'),
        ),
    ]
