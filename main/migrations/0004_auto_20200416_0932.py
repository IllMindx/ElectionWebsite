# Generated by Django 3.0.5 on 2020-04-16 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200416_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 12, 32, 31, 493603, tzinfo=utc), verbose_name='date joined'),
        ),
    ]