# Generated by Django 4.2.4 on 2023-11-12 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_car_owner_registration_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivinglicense',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.driver'),
        ),
    ]
