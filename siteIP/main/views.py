from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'dar': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def check(request):
    return render(request, 'main/check.html')


def Contacts(request):
    return render(request, 'main/Contacts.html')


def News(request):
    return render(request, 'main/News.html')


def Products(request):
    return render(request, 'main/Products.html')


def Services(request):
    return render(request, 'main/Services.html')


def scss(request):
    return render(request, 'main/scss.html')


def api(request):
    return render(request, 'main/api.html')




