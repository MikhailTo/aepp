
from django.shortcuts import render
from main.forms import calcSpeedForm

nav = [
    {'name': 'Главная',         'url': 'index'},
    {'name': 'Скорости',        'url': 'speed'},
    {'name': 'Наряды',          'url': 'order'},
    {'name': 'Расположение',    'url': 'location'},
    {'name': 'Склад',           'url': 'storage'},
    {'name': 'Инструкции',      'url': 'manuals'},
]



def index(request):

    data = {
        'name': 'index',
        'title': 'Главная страница',
        'nav': nav,
    }

    return render(request, 'main/index.html', context=data)


def speed(request):
    if request.method == 'POST':
        form = calcSpeedForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            result = get_memf(request.POST)
    else:
        form = calcSpeedForm(auto_id=True)
        result = ''

    data = {
        'name': 'speed',
        'title': 'Настройка скоростей',
        'nav': nav,
        'form': form,
        'result': result,
    }

    return render(request, 'main/speed.html', context=data)


def get_memf(data):
    med = 0.17
    rang = 2
    task = float(data['task'])
    tspd = float(data['tspd'])
    bmav = float(data['bmav'])
    bemf = float(data['bemf'])

    dtmav = abs(task * tspd - bmav)

    step = med * dtmav if not (-rang <= dtmav <= rang) else dtmav * 0

    result = bemf + step
    result = round(result, 2) if result % 1 != 0 else result
    return result


def order(request):
    data = {
        'name': 'order',
        'title': 'Наряды',
        'nav': nav,
    }
    return render(request, 'main/order.html', context=data)


def location(request):
    data = {
        'name': 'location',
        'title': 'Расположение',
        'nav': nav,
    }
    return render(request, 'main/location.html', context=data)


def storage(request):
    data = {
        'name': 'storage',
        'title': 'Склады',
        'nav': nav,
    }
    return render(request, 'main/storage.html', context=data)


def manuals(request):
    data = {
        'name': 'manuals',
        'title': 'Руководства по эксплуатации',
        'nav': nav,
    }
    return render(request, 'main/manuals.html', context=data)