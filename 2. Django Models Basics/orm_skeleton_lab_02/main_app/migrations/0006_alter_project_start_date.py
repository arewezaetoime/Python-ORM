# Generated by Django 4.2.4 on 2023-10-22 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_project_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start Date'),
        ),
    ]
