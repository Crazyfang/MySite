# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-13 07:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180413_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='article_tag',
            field=models.ManyToManyField(blank=True, related_name='article_tag', to='article.ArticleTag'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 13, 7, 25, 58, 574060, tzinfo=utc)),
        ),
    ]
