# Generated by Django 3.0.5 on 2020-04-20 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200416_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='candidate_voted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Candidate'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 17, 25, 32, 920002, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
