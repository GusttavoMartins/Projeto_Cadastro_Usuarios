from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuario/home.html')


def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    nome = f"{firstname} {lastname}"
    novo_usuario.nome = nome
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.data_nasc = request.POST.get('data')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.genero = request.POST.get('gender')
    novo_usuario.save()
    # Exibir dados cadastrados em uma nova pagina
    usuarios = {
        "usuarios": Usuario.objects.all()
    }
    # Retornar os dados para a pagina de lista
    return render(request, 'usuario/lista_usuarios.html', usuarios)
