# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author_comment',
            field=models.TextField(default='Default Comment'),
            preserve_default=False,
        ),
    ]