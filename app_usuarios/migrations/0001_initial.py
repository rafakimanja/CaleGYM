# Generated by Django 5.0.1 on 2024-01-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=25)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=4)),
                ('altura', models.IntegerField()),
                ('imc', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
        ),
    ]