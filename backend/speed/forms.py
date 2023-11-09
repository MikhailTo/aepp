from django import forms

class calcSpeedForm(forms.Form):
	labels = {
		"task":		"Задание с клином в привод, %",
		"tspd":		"Выставленная скорость по заданию, м/с",
		"fspd":		"Фактическая скорость на терминале, м/с",
		"bmav":		"Изм. угл. факт. скорость до корр., об/мин",
		"bemf":		"Значение параметра P115.2 до изменения",
		"amav":		"Изм. угл. факт. скорость после корр., об/мин",
		"aemf":		"Значение параметра P115.2 после изменения",
		"dtmav":	"Разница скоростей заданной от фактической, %",
	}

	task = forms.FloatField(label=labels["task"], min_value=0)
	tspd = forms.FloatField(label=labels["tspd"], min_value=0)
	bemf = forms.FloatField(label=labels["bemf"], min_value=0)
	bmav = forms.FloatField(label=labels["bmav"], min_value=0)

