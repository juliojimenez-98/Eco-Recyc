from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import QuienesSomos,index,Contactanos,Servicios,Login,register,home,logout,editarPerfil

urlpatterns = [
    path('', index, name="index"),
    path('QuienesSomos.html', QuienesSomos, name="QuienesSomos"),
    path('Contactanos.html', Contactanos, name="Contactanos"),
    path('Servicios.html', Servicios, name="Servicios"),
    path('Login.html',Login, name="Login"),
    path('logout', logout),
    path('register.html',register, name="register"),
    path('home.html',home, name="home"),
    path('editarPerfil.html', editarPerfil, name="editarPerfil"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
