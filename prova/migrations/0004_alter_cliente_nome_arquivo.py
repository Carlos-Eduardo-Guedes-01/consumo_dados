# Generated by Django 4.1.3 on 2022-12-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0003_alter_cliente_altura_alter_cliente_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome_arquivo',
            field=models.FileField(null=True, upload_to='prova/media'),
        ),
    ]
