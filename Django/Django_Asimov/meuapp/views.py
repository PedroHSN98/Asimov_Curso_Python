from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    hora_atual = datetime.now().hour

    if 5 <= hora_atual < 12:
        mensagem = 'Bom Dia!'
    elif 12 <= hora_atual < 18:
        mensagem = 'Boa Tarde!'
    else:
        mensagem = 'Boa Noite!'
    return HttpResponse(mensagem)

def saudacao(request, nome):
    mensagem = (f'Olá, {nome}! Bem vindo(a) ao nosso site.')
    return HttpResponse(mensagem)

def produtos(request, id_produto):

    produtos = {
        1:'Notebook',
        2:'Teclado',
        3:'Mouse',
    }

    produto = produtos.get(id_produto, 'Produto não encontrado!')
    return HttpResponse(f'Detalhes do produto: {produto}')

def frutas(request, id_fruta):

    frutas = {
        1:'Melancia',
        2:'Uva',
        3:'Manga',
        4:'Laranja',
        5:'Morango',
    }

    fruta = frutas.get(int(id_fruta), 'Fruta não encontrada!')
    return HttpResponse(f'Detalhes da fruta selecionada: {fruta}')             