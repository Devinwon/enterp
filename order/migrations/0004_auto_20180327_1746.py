# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-27 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180327_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='Code',
            field=models.IntegerField(),
        ),
    ]
