# Generated by Django 2.2.7 on 2019-11-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_usuario_nusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_mision',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='realizado_mision',
            field=models.IntegerField(null=True),
        ),
    ]
