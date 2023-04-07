
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name = 'home'),
    path('price', views.price, name = 'price'),
    path('info', views.info, name = 'info'),
    path('index', views.index, name = 'index')
]



