# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160430_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='codetext',
            name='is_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ManyToManyField(related_name='author', to='blog.Author'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.ManyToManyField(related_name='code_text', to='blog.CodeText'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
    ]
