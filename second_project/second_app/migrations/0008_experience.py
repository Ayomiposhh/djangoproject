# Generated by Django 4.0.6 on 2022-08-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
