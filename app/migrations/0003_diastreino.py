# Generated by Django 5.0.1 on 2024-01-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pessoa_peso'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasTreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treino', models.BooleanField()),
                ('registro', models.DateTimeField()),
            ],
        ),
    ]
