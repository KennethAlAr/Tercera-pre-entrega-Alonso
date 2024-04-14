# Generated by Django 5.0.4 on 2024-04-14 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='juego',
            name='hora_fin',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='juego',
            name='hora_inicio',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]