# Generated by Django 4.0.6 on 2022-08-02 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('second_app', '0003_alter_blog_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('slug', models.SlugField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('image', models.ImageField(upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
