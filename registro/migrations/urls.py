from django.urls import path
from registro import views

app_name = 'registro'

urlpatterns = [
    path('registro/', views.registro,name='registro'),
]
