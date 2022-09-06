# Generated by Django 4.1 on 2022-09-06 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('removed', models.BooleanField(default=False)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('altitude', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Pollutant',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('removed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'pollutants',
            },
        ),
        migrations.CreateModel(
            name='PollutantEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('station_code', models.CharField(blank=True, default='', max_length=20)),
                ('station_name', models.CharField(blank=True, default='', max_length=100)),
                ('pollution_level', models.FloatField()),
                ('units', models.CharField(blank=True, default='', max_length=10)),
                ('station_type', models.CharField(blank=True, default='', max_length=20)),
                ('station_area', models.CharField(blank=True, default='', max_length=20)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('altitude', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='airpollution.country')),
                ('pollutant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='airpollution.pollutant')),
            ],
            options={
                'verbose_name_plural': 'pollutant entries',
            },
        ),
    ]
