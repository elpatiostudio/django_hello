from django.shortcuts import render


def home(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
        'features': ['cheap', 'fast', 'easy', ],
    }
    return render(request, 'home.html', context)


def contact(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'contact.html', context)

def products(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'products.html', context)

def services(request):
    name = request.GET.get('name', 'User')
    context = {
        'name': name,
    }
    return render(request, 'services.html', context)



