# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-03 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='url_path',
            field=models.URLField(blank=True),
        ),
    ]