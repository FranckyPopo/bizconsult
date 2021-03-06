# Generated by Django 4.0.4 on 2022-06-14 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_alter_about_created_alter_contactcompany_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 779460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 785991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='designation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 785046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 780794, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredescription',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 780397, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='indexfront',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 778444, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logocompany',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 781188, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 780008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='image',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 785445, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 14, 16, 8, 784582, tzinfo=utc)),
        ),
    ]
