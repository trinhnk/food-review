# Generated by Django 3.2.8 on 2021-10-19 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.CharField(max_length=255, verbose_name='image')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('excerpt', models.CharField(max_length=500, verbose_name='excerpt')),
                ('content', models.TextField(verbose_name='content')),
                ('score', models.IntegerField(blank=True, default=0, verbose_name='score')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('modified', models.DateTimeField(null=True, verbose_name='modified')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
            ],
        ),
    ]