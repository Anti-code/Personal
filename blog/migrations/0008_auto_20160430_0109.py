# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160430_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='body',
        ),
        migrations.AddField(
            model_name='entry',
            name='body',
            field=models.ManyToManyField(to='blog.CodeText'),
        ),
    ]
