# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amh_api', '0003_auto_20151206_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(to='amh_api.Team'),
        ),
    ]
