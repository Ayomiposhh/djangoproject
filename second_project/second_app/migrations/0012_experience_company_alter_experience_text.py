# Generated by Django 4.0.6 on 2022-08-05 18:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0011_remove_experience_content_experience_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='text',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
    ]
