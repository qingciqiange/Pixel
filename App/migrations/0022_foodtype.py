# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-12 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0021_delete_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField(default=1)),
                ('typename', models.CharField(max_length=32)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtype',
            },
        ),
    ]
