# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0006_auto_20180508_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], max_length=50)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('name', 'page')]),
        ),
    ]
