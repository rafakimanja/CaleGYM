# Generated by Django 5.0.1 on 2024-01-08 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_diastreino_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diastreino',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 2, 38, 15, 62232)),
        ),
    ]
