# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 16:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('size', models.CharField(max_length=32, null=True, validators=[django.core.validators.RegexValidator(message='Enter L,W,H as numbers in meters', regex='^(\\d*\\.\\d+|\\d+),(\\d*\\.\\d+|\\d+),(\\d*\\.\\d+|\\d+)$')])),
                ('weight', models.FloatField(null=True)),
                ('unit_of_issue', models.CharField(default='EACH', max_length=8)),
                ('quantity', models.IntegerField()),
                ('last_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+999999999' without separators.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer'),
        ),
    ]
