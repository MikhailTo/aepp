import boto3
from decouple import config
from django.shortcuts import render
from .forms import calcSpeedForm, createOrder


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
    form = createOrder(auto_id=True)
    data = {
        'name': 'order',
        'title': 'Наряды',
        'nav': nav,
        'form': form,
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


def getManuals(s3, bucket):
    manuals = []
    for key in s3.list_objects(Bucket=bucket)['Contents']:
        if key['Key'][0:13] == 'data/manuals/' and key['Key'][-3:] == 'pdf':
            name = ' '.join(key['Key'][:-4].split('/')[2:])
            url = 'https://storage.yandexcloud.net/aepp.ru/' + key['Key']
            manuals.append({'name': name, 'url': url})
    return manuals


def manuals(request):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        region_name=config('REGION_NAME'),
        aws_access_key_id=config('ACCESS_KEY'),
        aws_secret_access_key=config('SECRET_KEY')
    )

    bucket_name = 'aepp.ru'
    manuals = getManuals(s3, bucket_name)


    data = {
        'name': 'manuals',
        'title': 'Руководства по эксплуатации',
        'nav': nav,
        'manuals': manuals,
    }


    return render(request, 'main/manuals.html', context=data)