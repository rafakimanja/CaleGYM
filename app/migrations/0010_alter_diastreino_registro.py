# Generated by Django 5.0.1 on 2024-01-08 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_diastreino_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diastreino',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 2, 25, 31, 697817, tzinfo=datetime.timezone.utc)),
        ),
    ]