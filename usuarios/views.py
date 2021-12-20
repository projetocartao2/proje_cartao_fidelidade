from django.shortcuts import redirect, render
from .models import Usuarios
from .forms import UsuarioForm

# Create your views her

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios' : usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form =  UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})