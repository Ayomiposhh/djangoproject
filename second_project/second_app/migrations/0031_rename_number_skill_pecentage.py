# Generated by Django 4.0.6 on 2022-08-16 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0030_remove_skill_percentage_skill_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='number',
            new_name='pecentage',
        ),
    ]