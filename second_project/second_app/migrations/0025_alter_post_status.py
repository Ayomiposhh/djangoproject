# Generated by Django 4.0.6 on 2022-08-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0024_alter_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=2),
        ),
    ]
