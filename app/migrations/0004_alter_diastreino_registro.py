# Generated by Django 5.0.1 on 2024-01-08 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_diastreino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diastreino',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 1, 46, 38, 883111, tzinfo=datetime.timezone.utc)),
        ),
    ]