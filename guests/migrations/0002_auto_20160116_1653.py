# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='guest',
            name='last_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
