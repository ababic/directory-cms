# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-15 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0009_auto_20180813_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicslug',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterUniqueTogether(
            name='historicslug',
            unique_together=set([('slug', 'page')]),
        ),
    ]
