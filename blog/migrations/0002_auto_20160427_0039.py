# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ManyToManyField(to='blog.Author'),
        ),
        migrations.AddField(
            model_name='entry',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
