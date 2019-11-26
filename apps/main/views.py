from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from apps.main.models import usuario,misiones,registro,premios

# Create your views here.

def index(request):
    return render(request,'main/index.html')

def QuienesSomos(request):
    return render(request,'main/QuienesSomos.html')

def Contactanos(request):
    return render(request,'main/Contactanos.html')

def Servicios(request):
    return render(request,'main/Servicios.html')

def Login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            usuario = authenticate(password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user, usuario)
                # Y le redireccionamos a la portada
                return redirect('home')
    return render(request, "main/Login.html", {'form': form})

def register(request):
 # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        nusuario = request.POST['nusuario']
        fnacimiento = request.POST['fnacimiento']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        regUsuarios = usuario.objects.create(nombre_usuario=nombre,apellido_usuario=apellido,correo_usuario=correo,fecha_Nacimiento=fnacimiento,nusuario=nusuario,clave_usuario=contraseña)

        user = User.objects.create_user( first_name=nombre, last_name=apellido, username=nusuario, email=correo, password=contraseña)
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user.save()
            regUsuarios.save()
            print('usuario creado')

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "main/register.html", {'form': form})    


def home(request):

    user = User.objects.all()

    obUsuario = usuario.objects.all()

    mision = misiones.objects.get(id=2)

    misionRealizada = registro.objects.all()


    context = {'obUsuario':obUsuario, 'mision':mision, 'misionRealizada':misionRealizada}
    if request.method == "POST":
        #TABLA REGISTRO
        txtImagen = request.FILES['txtImagen']
        subirImagen = registro.objects.create(imagen_mision=txtImagen,realizado_mision=0)
   # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "main/home.html",context)
    return redirect('Login')

def logout(request):
     do_logout(request) 
     return redirect('index')    

def editarPerfil(request):
    return render(request,'main/editarPerfil.html')    