# Generated by Django 4.2.4 on 2023-11-15 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeltbladeDemonHunter',
            new_name='FelbladeDemonHunter',
        ),
        migrations.RenameField(
            model_name='assassin',
            old_name='demon_slaying_ability',
            new_name='assassination_technique',
        ),
        migrations.RenameField(
            model_name='felbladedemonhunter',
            old_name='feldblade_ability',
            new_name='felblade_ability',
        ),
    ]
