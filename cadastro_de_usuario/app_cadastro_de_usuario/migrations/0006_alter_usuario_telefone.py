# Generated by Django 4.2.3 on 2023-07-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_de_usuario', '0005_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.IntegerField(null=True),
        ),
    ]