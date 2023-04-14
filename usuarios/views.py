from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
import password_strength

def cadastro(request):
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):    
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect(reverse('cadastro'))
        
        ##TODO: validar força da senha
        password_policy = password_strength.PasswordPolicy.from_names(
            length=8,  # mínimo de 8 caracteres
            uppercase=1,  # pelo menos 1 letra maiúscula
            numbers=1,  # pelo menos 1 número
            special=1,  # pelo menos 1 caractere especial
            nonletters=1,  # pelo menos 1 caractere que não seja letra
        )

        if password_policy.test(senha):
            messages.add_message(request, constants.SUCCESS, 'Senha forte!')
        else:
            messages.add_message(request, constants.WARNING, 'Senha fraca. Use uma senha mais forte. Dicas: mínimo de 8 caracteres com pelo menos 1 letra maiúscula, pelo menos 1 número, pelo menos 1 caractere especial, pelo menos 1 caractere que não seja letra')
            return redirect(reverse('cadastro'))
        
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')
            return redirect(reverse('cadastro'))   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso!')
        return redirect(reverse('login'))
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')