# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20160729_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]