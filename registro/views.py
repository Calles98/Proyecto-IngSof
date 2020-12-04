from django.shortcuts import render
from registro.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from registro.models import UserProfileInfo
from home import views
# Create your views here.



@login_required
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def registro(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()


    return render(request,'registro/registro.html',{'user_form':user_form,'registered':registered})



def login_usuario(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('CUENTA NO ACTIVA')

        else:
            print("Alguien intentó ingresar y falló")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Datos invalidos para login")
    else:
        return render(request,'registro/login.html', {})
