from django.urls import path
from registro import views

app_name = 'registro'

urlpatterns = [
    path('registro/', views.registro,name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout', views.logout_usuario, name='logout'),
]
