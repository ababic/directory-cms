# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-03 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0026_auto_20180329_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ar',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_de',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_en_gb',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_es',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_fr',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ja',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_pt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_pt_br',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_breadcrumb_label_zh_hans',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_en_gb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_pt_br',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_button_text_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_introduction_text_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
    ]