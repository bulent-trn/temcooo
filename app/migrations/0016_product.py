# Generated by Django 4.1.4 on 2022-12-23 21:52

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_tagdict_blog_date_created_blog_date_published_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('description', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('date_published', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
