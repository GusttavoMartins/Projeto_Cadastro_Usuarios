# Generated by Django 4.2.3 on 2023-07-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_de_usuario', '0004_rename_emial_usuario_email_alter_usuario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.TextField(max_length=25),
        ),
    ]
