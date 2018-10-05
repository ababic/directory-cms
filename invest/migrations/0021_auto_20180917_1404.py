# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0008_document_file_size'),
        ('invest', '0020_auto_20180917_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highpotentialopportunitydetailpage',
            name='pdf_document_url',
        ),
        migrations.AddField(
            model_name='highpotentialopportunitydetailpage',
            name='pdf_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]