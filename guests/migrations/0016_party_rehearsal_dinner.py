# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-19 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0015_party_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='rehearsal_dinner',
            field=models.BooleanField(default=False),
        ),
    ]
