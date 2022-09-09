# Generated by Django 4.1 on 2022-09-08 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'RENT'), (2, 'BILLS'), (3, 'CAR'), (4, 'TRAVEL'), (5, 'HEALTH'), (6, 'GROCERIES'), (7, 'FUN'), (8, 'CLOTHES'), (9, 'CHARITY'), (10, 'SAVINGS')])),
                ('repetitive', models.BooleanField(default=False)),
                ('repetition_interval', models.PositiveSmallIntegerField(choices=[(1, 'N/A'), (2, 'DAYS'), (3, 'WEEKS'), (4, 'MONTHS'), (5, 'YEARS')], default=1)),
                ('repetition_time', models.PositiveSmallIntegerField(default=0)),
                ('repetition_end', models.DateField(null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'outcomes',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'SALARY'), (2, 'BONUS'), (3, 'GIFT'), (4, 'OTHER'), (5, 'SAVINGS')])),
                ('repetitive', models.BooleanField(default=False)),
                ('repetition_interval', models.PositiveSmallIntegerField(choices=[(1, 'N/A'), (2, 'DAYS'), (3, 'WEEKS'), (4, 'MONTHS'), (5, 'YEARS')], default=1)),
                ('repetition_time', models.PositiveSmallIntegerField(default=0)),
                ('repetition_end', models.DateField(null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'incomes',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'CURRENT'), (2, 'SAVINGS')])),
                ('date', models.DateField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'balances',
            },
        ),
    ]