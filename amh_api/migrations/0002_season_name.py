# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amh_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='name',
            field=models.CharField(default='A', max_length=255),
        ),
    ]