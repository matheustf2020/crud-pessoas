from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from .models import Pessoa, Cargos, Projetos

def criar_pessoa(request):
    if request.method == "GET":
        return render(request, 'criar_pessoa.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        cargo = Cargos.objects.get(id=1)
        if Pessoa.objects.filter(nome=nome).exists():
            return HttpResponse('Nome já existe, tente outro nome')
        elif len(senha) < 4:
            return HttpResponse('Senha menor que 4 caracteres')
        else:
            pessoa = Pessoa(
                            nome = nome,
                            senha = senha,
                            email = email,
                            cargo = cargo
            )
            pessoa.save()
            return redirect('listar_pessoas')
            
    

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})
    

def criar_projeto(request):
    if request.method == "GET":
        return render(request, 'criar_projeto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        pessoa = Projetos(
                            nome = nome,
                            descricao = descricao
        )
        pessoa.save()
        return redirect('listar_projetos')

def deletar_projeto(request, id):
    if request.method == "GET":
        buscar = get_object_or_404(Projetos, id=id)
        return render(request, 'deletar_projeto.html', {'buscar': buscar})
    elif request.method == "POST":
        buscar = get_object_or_404(Projetos, id=id)
        buscar.delete()
        return redirect('listar_projetos')

def listar_projetos(request):
    projetos = Projetos.objects.all()
    return render(request, 'listar_projetos.html', {'projetos': projetos})

def vincular_pessoas(request, id):
    projeto = get_object_or_404(Projetos, id=id)

    if request.method == "POST":
        pessoas_ids = request.POST.getlist('pessoas')  # lista de IDs marcados no formulário
        for pessoa_id in pessoas_ids:
            pessoa = Pessoa.objects.get(id=pessoa_id)
            projeto.pessoa_set.add(pessoa)

        return redirect('listar_projetos')

    pessoas = Pessoa.objects.all()
    return render(request, 'vincular_pessoas.html', {'projeto': projeto, 'pessoas': pessoas})


def editar_pessoa(request, id):
    if request.method == "GET":
        buscar = Pessoa.objects.get(id=id)
        return render(request, 'editar_pessoa.html', {'pessoa': buscar})
    elif request.method == "POST":
        buscar = Pessoa.objects.get(id=id)
        novo_nome = request.POST.get('nome')
        nova_senha = request.POST.get('senha')
        novo_email = request.POST.get('email')

        buscar.nome = novo_nome
        buscar.email = novo_email
        buscar.senha = nova_senha

        buscar.save()
        return redirect('listar_pessoas')

def deletar_pessoa(request, id):
    if request.method == "GET":
        buscar = Pessoa.objects.get(id=id)
        return render(request, 'deletar_pessoa.html', {'pessoa': buscar})
    elif request.method == "POST":
        buscar = Pessoa.objects.get(id=id)
        buscar.delete()
        return redirect('listar_pessoas')


