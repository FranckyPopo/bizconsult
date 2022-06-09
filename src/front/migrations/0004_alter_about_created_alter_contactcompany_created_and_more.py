# Generated by Django 4.0.4 on 2022-06-09 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_alter_about_created_alter_contactcompany_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 94879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 154098, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='instagram_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='likedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactcompany',
            name='youtube_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='designation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 152099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 102878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredescription',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 100879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='indexfront',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 91879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logocompany',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 104879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 97878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 153099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 12, 2, 41, 152099, tzinfo=utc)),
        ),
    ]