# Generated by Django 5.0.1 on 2024-01-12 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_diastreino_registro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.AlterField(
            model_name='diastreino',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 12, 28, 15, 892300)),
        ),
    ]
