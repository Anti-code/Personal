# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 00:27
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
