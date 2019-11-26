from django.db import models

# Create your models here.
class usuario(models.Model):

    nombre_usuario = models.CharField(max_length=30)
    apellido_usuario= models.CharField(max_length=30)
    fecha_Nacimiento = models.DateField(null=True)
    correo_usuario = models.CharField(max_length=50)
    telefono_usuario = models.IntegerField(null=True)
    nusuario = models.CharField(max_length=50)
    clave_usuario = models.CharField(max_length=15,null=True)
    puntos_usuario = models.IntegerField(null=True)   


class misiones(models.Model):

    descripcion_mision = models.CharField(max_length=1000)
    puntaje_mision = models.IntegerField()
    

class registro(models.Model):

    fecha_mision = models.DateField(auto_now_add= True)
    realizado_mision = models.IntegerField(null=True)
    imagen_mision = models.ImageField(upload_to="Misiones", null=True)
    Id_u = models.ForeignKey(usuario,null = True, blank=True, on_delete=models.DO_NOTHING) 
    Id_m = models.ForeignKey(misiones,null = True, blank=True, on_delete=models.DO_NOTHING) 

class puntosLimpios(models.Model):

    direccion_punto = models.CharField(max_length=100)
    nombre_punto = models.CharField(max_length=100)
    foto_punto = models.ImageField()
    descripcion_punto = models.CharField(max_length=100)

class premios(models.Model):

    costo_premio = models.IntegerField()
    descripcion_premio = models.CharField(max_length=1000)
    imagen_premio = models.ImageField()

class usuarioPremio(models.Model):

    fechaObtencion = models.DateTimeField() 
    Id_u = models.ForeignKey(usuario,null = True, blank=True, on_delete=models.DO_NOTHING) 
    Id_p = models.ForeignKey(premios,null = True, blank=True, on_delete=models.DO_NOTHING) 