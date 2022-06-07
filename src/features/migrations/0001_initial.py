# Generated by Django 4.0.5 on 2022-06-07 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 6, 7, 12, 22, 16, 316834, tzinfo=utc))),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 6, 7, 12, 22, 16, 314834, tzinfo=utc))),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 6, 7, 12, 22, 16, 315834, tzinfo=utc))),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
