from django.shortcuts import render
from .models import estados,Usuario
# Create your views here.


def home(request):
    return render(request,'page/home.html')

def procura(request):
    resultado = estados.objects.all
    return render(request,'page/procura.html', {"showestados":resultado})


def registro(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.estado = request.POST.get('estado')
    novo_usuario.save()

    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'page/registro.html',usuarios)

def registros(request):

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'page/registros.html', usuarios)