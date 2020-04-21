# Generated by Django 3.0.5 on 2020-04-15 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('number', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('card_id', models.PositiveIntegerField(unique=True)),
                ('password', models.CharField(max_length=60)),
                ('role', models.CharField(choices=[('Voter', 'Voter'), ('Inspector', 'Inspector'), ('Admin', 'Admin')], max_length=20)),
                ('candidate_voted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Candidate')),
            ],
        ),
    ]
