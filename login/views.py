from unicodedata import name
from django.shortcuts import render
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
#from login.models import Parque, Senha, User


#def login(request):
 #   if request.user.is_authenticated:
        #return redirect('/plataforma/home')
  #      return HttpResponse("Logado")
   # status = request.GET.get('status')
    #print("Status: ")
    #print(status)
    #return render(request, 'login.html', {'status': status})
    #return render(request,"login.html")



def login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    
    usuario = auth.authenticate(username = nome, password = senha)
    print(usuario)
    if not usuario:
        messages.add_message(request, constants.WARNING, 'Email ou senha inválido')
        #return redirect('/auth/login/')
        return HttpResponse("Email ou senha inválido")
    else:
        auth.login(request, usuario)
        #return redirect('/plataforma/home')
        return HttpResponse("Usuario logado")


def Logar(request):
    
    return render(request,"login.html")


@login_required(login_url="/auth/logar")
def home(request):
    #if request.user.is_authenticated:
    return HttpResponse("Tela proibida")

    #return HttpResponse("Você precisa estar logado")



#def index(request):
    
    
    #print(request.user.parque)
    
    #print(request.user)
    #print("_______________/n")
    #Listando todas senha do parque onildo maior que percence ao usuario hitalo
    #senha = Senha.objects.all().filter(parque = request.user.parque) 
    #context = {'senha': senha,'usuario':request.user}
    #print("lista de senhas: ")
    #print("Usuario Logado: ")
    
    #for s in senha:
        #print("Vaqueiro: " )
        #print(s)
        #print("Representação: ")
        #print(s.Representacao)

    #return HttpResponse(senha)
    #return render(request, 'login.html', context)