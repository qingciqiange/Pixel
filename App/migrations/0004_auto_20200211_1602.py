# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-11 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200211_1602'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='mainnav',
            table='axf_nav',
        ),
    ]
