# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import guests.models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_guest_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='invitation_id',
            field=models.CharField(blank=True, db_index=True, default=guests.models._random_uuid, max_length=32, null=True),
        ),
    ]
