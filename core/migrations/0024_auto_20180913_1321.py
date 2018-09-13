# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20180912_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagehash',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
    ]
