# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 03:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prerequisite', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='credtype',
        ),
        migrations.RemoveField(
            model_name='course',
            name='days',
        ),
        migrations.RemoveField(
            model_name='course',
            name='icons',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructors',
        ),
        migrations.RemoveField(
            model_name='course',
            name='prereqs',
        ),
        migrations.AddField(
            model_name='course',
            name='course_date',
            field=models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='requirements',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.Course'),
        ),
        migrations.AddField(
            model_name='prerequisites',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.Course'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.Course'),
        ),
        migrations.AddField(
            model_name='days',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.Course'),
        ),
        migrations.AddField(
            model_name='conditions',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.Course'),
        ),
    ]
