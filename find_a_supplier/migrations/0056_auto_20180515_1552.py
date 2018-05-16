# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-15 15:52
from __future__ import unicode_literals

from wagtail.core.models import Page

from django.db import migrations


def set_industry_options(apps, schema_editor):
    IndustryContactPage = apps.get_model(
        'find_a_supplier', 'IndustryContactPage'
    )
    page = IndustryContactPage.objects.first()
    if page:
        page.industry_options = [
            'AEROSPACE',
            'ADVANCED_MANUFACTURING',
            'AIRPORTS',
            'AGRICULTURE_HORTICULTURE_AND_FISHERIES',
            'AUTOMOTIVE',
            'BIOTECHNOLOGY_AND_PHARMACEUTICALS',
            'BUSINESS_AND_CONSUMER_SERVICES',
            'CHEMICALS',
            'CLOTHING_FOOTWEAR_AND_FASHION',
            'COMMUNICATIONS',
            'CONSTRUCTION',
            'CREATIVE_AND_MEDIA',
            'EDUCATION_AND_TRAINING',
            'ELECTRONICS_AND_IT_HARDWARE',
            'ENVIRONMENT',
            'FINANCIAL_AND_PROFESSIONAL_SERVICES',
            'FOOD_AND_DRINK',
            'GIFTWARE_JEWELLERY_AND_TABLEWARE',
            'GLOBAL_SPORTS_INFRASTRUCTURE',
            'HEALTHCARE_AND_MEDICAL',
            'HOUSEHOLD_GOODS_FURNITURE_AND_FURNISHINGS',
            'LIFE_SCIENCES',
            'LEISURE_AND_TOURISM',
            'LEGAL_SERVICES',
            'MARINE',
            'MECHANICAL_ELECTRICAL_AND_PROCESS_ENGINEERING',
            'METALLURGICAL_PROCESS_PLANT',
            'METALS_MINERALS_AND_MATERIALS',
            'MINING',
            'OIL_AND_GAS',
            'PORTS_AND_LOGISTICS',
            'POWER',
            'RAILWAYS',
            'RENEWABLE_ENERGY',
            'RETAIL_AND_LUXURY',
            'SECURITY',
            'SOFTWARE_AND_COMPUTER_SERVICES',
            'TEXTILES_INTERIOR_TEXTILES_AND_CARPETS',
            'WATER'
        ]
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0055_industrycontactpage_industry_options'),
    ]

    operations = [
        migrations.RunPython(set_industry_options, migrations.RunPython.noop)
    ]
