# Generated by Django 2.2.6 on 2019-11-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191119_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='imagen_mision',
            field=models.ImageField(null=True, upload_to='Misiones'),
        ),
    ]
