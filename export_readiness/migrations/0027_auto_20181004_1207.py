# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 12:07
from __future__ import unicode_literals

from django.db import migrations


def add_tags(apps, schema_migrations):
    Tag = apps.get_model('export_readiness', 'Tag')
    Tag.objects.bulk_create([
        Tag(name='Legal'),
        Tag(name='Accessing markets'),
        Tag(name='Tariffs'),
        Tag(name='New to exporting'),
        Tag(name='Trade restrictions'),
        Tag(name='Export tips'),
        Tag(name='Regulations'),
        Tag(name='Exporting to EU countries'),
        Tag(name='Importing from EU countries'),
        Tag(name='Free economic zones'),
        Tag(name='Tax'),
        Tag(name='Duty')
    ])


def remove_tags(apps, schema_migrations):
    tag_names = [
        'Legal',
        'Accessing markets',
        'Tariffs',
        'New to exporting',
        'Trade restrictions',
        'Export tips',
        'Regulations',
        'Exporting to EU countries',
        'Importing from EU countries',
        'Free economic zones',
        'Tax',
        'Duty'
    ]

    Tag = apps.get_model('export_readiness', 'Tag')
    Tag.objects.filter(name__in=tag_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0026_tag_slug'),
    ]

    operations = [
        migrations.RunPython(add_tags, reverse_code=remove_tags)
    ]
