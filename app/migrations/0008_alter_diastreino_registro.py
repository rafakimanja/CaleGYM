# Generated by Django 5.0.1 on 2024-01-08 02:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_diastreino_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diastreino',
            name='registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]