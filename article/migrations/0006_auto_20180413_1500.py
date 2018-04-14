# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-13 07:00
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_auto_20180412_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 13, 7, 0, 2, 41728, tzinfo=utc)),
        ),
    ]