# Generated by Django 5.0.1 on 2024-01-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usuarios', '0002_alter_usuario_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]