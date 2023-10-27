# Generated by Django 4.2.4 on 2023-10-27 14:11

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(default=datetime.datetime(2023, 10, 27, 14, 11, 30, 222487, tzinfo=datetime.timezone.utc), max_length=150),
            preserve_default=False,
        ),
    ]
