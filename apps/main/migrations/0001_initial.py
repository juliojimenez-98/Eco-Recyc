# Generated by Django 2.2.3 on 2019-10-15 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='misiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_mision', models.CharField(max_length=1000)),
                ('puntaje_mision', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='premios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_premio', models.IntegerField()),
                ('descripcion_premio', models.CharField(max_length=1000)),
                ('imagen_premio', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='puntosLimpios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_punto', models.CharField(max_length=100)),
                ('nombre_punto', models.CharField(max_length=100)),
                ('foto_punto', models.ImageField(upload_to='')),
                ('descripcion_punto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('apellido_usuario', models.CharField(max_length=30)),
                ('fecha_Nacimiento', models.DateField()),
                ('correo_usuario', models.CharField(max_length=50)),
                ('telefono_usuario', models.IntegerField()),
                ('clave_usuario', models.CharField(max_length=15)),
                ('puntos_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuarioPremio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaObtencion', models.DateTimeField()),
                ('Id_p', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.premios')),
                ('Id_u', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_mision', models.DateField()),
                ('realizado_mision', models.IntegerField()),
                ('imagen_mision', models.ImageField(upload_to='')),
                ('Id_m', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.misiones')),
                ('Id_u', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.usuario')),
            ],
        ),
    ]
