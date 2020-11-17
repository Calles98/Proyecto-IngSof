from django.shortcuts import render
from registro.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def registro(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            #user = user_form.save()
            #user.set_password(user.password)
            user_form.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'registro/registro.html',{'user_form':user_form,'registered':registered})






# def registro(request):
#     registered = False
#     if request.method == "POST":
#         user_form = UserForm(data=request.POST)
#
#         if user_form.is_valid():
#
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             registered = True
#
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserForm()
#         #profile_form = UserProfileInfoForm()
#
#     return render(request,'registro/registro.html',{'user_form':user_form,'registered':registered})
