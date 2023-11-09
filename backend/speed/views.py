from django.shortcuts import render
from .forms import calcSpeedForm


def index(request):
	if request.method == 'POST':
		form = calcSpeedForm(request.POST)
		if form.is_valid():
			print(form.changed_data)
	else:
		form = calcSpeedForm(auto_id=True)

	result = get_memf(request.POST)

	data = {
		'title': 'Настройка скоростей',
		'form': form,
		'result': result,
	}

	return render(request, 'speed/index.html', context=data)


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