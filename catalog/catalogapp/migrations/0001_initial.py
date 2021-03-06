# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('credtype', models.TextField()),
                ('prereqs', models.TextField()),
                ('icons', models.TextField()),
                ('course_id', models.IntegerField()),
                ('section', models.TextField()),
                ('credits', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('enrolled', models.IntegerField()),
                ('instructors', models.TextField()),
                ('start_end', models.TextField()),
                ('days', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
    ]
