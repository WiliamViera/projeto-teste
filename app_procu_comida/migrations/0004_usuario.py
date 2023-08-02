# Generated by Django 4.2.3 on 2023-07-31 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_procu_comida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
                ('estado', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
    ]
