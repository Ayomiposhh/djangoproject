# Generated by Django 4.0.6 on 2022-08-17 12:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0037_about_content_about_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='name',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]