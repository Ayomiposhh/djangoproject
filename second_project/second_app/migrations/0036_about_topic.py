# Generated by Django 4.0.6 on 2022-08-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0035_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='topic',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
