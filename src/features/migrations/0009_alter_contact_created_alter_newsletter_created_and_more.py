# Generated by Django 4.0.4 on 2022-06-14 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_alter_contact_created_alter_newsletter_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 784208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 783476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quote',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 783840, tzinfo=utc)),
        ),
    ]
