# Generated by Django 5.0.1 on 2024-01-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]