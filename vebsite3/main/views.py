from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(reqest):
    return render(reqest, 'main/index.html')


def price(reqest):
    return render(reqest, 'main/price.html')

def info(reqest):
    return render(reqest, 'main/info.html' )

def index(reqest):
    return render(reqest, 'main/index.html' )

# def create(reqest):
#     form = TaskForm
#     context = {"form": form}
#     return render(reqest, 'main/create.html', {'widgets': context})

# def skill(reqest):
#     return HttpResponse('<h4> Мощная страница </h4>')
#
# def sky(reqest):
#     return HttpResponse('<h1> Создал новую страницу </h1>')