# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-03-13 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_auto', '0022_garcom_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='numero_mesa',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
