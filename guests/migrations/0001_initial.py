# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('is_attending', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.CharField(choices=[('formal', 'formal'), ('fun', 'fun')], max_length=10)),
                ('save_the_date_sent', models.DateTimeField(default=None, null=True)),
                ('save_the_date_opened', models.DateTimeField(default=None, null=True)),
                ('is_invited', models.BooleanField(default=False)),
                ('is_attending', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guests.Party'),
        ),
    ]
