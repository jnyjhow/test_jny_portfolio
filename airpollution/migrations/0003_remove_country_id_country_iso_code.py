# Generated by Django 4.1 on 2022-09-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0002_remove_pollutantentry_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AddField(
            model_name='country',
            name='iso_code',
            field=models.CharField(default='AA', max_length=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
