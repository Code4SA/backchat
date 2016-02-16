# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 14:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('remote_ip', models.CharField(help_text=b"User's remote IP", max_length=20)),
                ('user_agent', models.CharField(help_text=b"User's user agent string", max_length=200)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(help_text=b'Raw submission from the user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
