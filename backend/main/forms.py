from django import forms
from .models import Company, Division, Issuer, Member, Watching

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

# class OrderForm(forms.ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = "__all__"
#
# 		def __init__(self, *args, **kwargs):
# 			super().__init__(*args, **kwargs)
# 			self.fields['division'].queryset = Division.objects.none()
#
class OrderForm(forms.Form):
	labels = {
		"company": "Организация",
		"division": "Подразделение",
		"order_number": "Наряд-допуск №",
		"accountable_name": "Ответственный руководитель работ",
		"allower_name": "Допускающий",
		"issuer": "Выдующий",
		"producer": "Производитель работ",
		"watching": "Наблюдающий",
		"brigade": "Члены бригады",
		"errand": "Поручения",
		"add_instrs": "Отдельные указания",
		"extrad_time": "Выдача наряда",
		"start_time": "Начало работы",
		"end_time": "Окончание работы",
		"interventions": {
			"installation_name": "Наименование электро-установок",
			"disconnections": "Отключения и заземления",
			"protections": "Ограждения",
		},
	}

	company = forms.ModelChoiceField(label=labels["company"],
										queryset=Company.objects.all(),
									 	# initial=Company.objects.get(pk=1),
										widget=forms.Select(attrs={'id': 'company', 'class': 'company'}))
	division = forms.ModelChoiceField(label=labels["division"],
										queryset=Division.objects.all(),
									  widget=forms.Select(attrs={'id': 'division', 'class': 'division'}))
	order_number = forms.IntegerField(label=labels["order_number"],
									  widget=forms.NumberInput(attrs={'class': 'order-number'}))
	accountable_name = forms.ModelChoiceField(label=labels["accountable_name"], queryset=Member.objects.all())
	allower_name = forms.ModelChoiceField(label=labels["allower_name"], queryset=Member.objects.all())
	producer = forms.ModelChoiceField(label=labels["producer"], queryset=Member.objects.all())
	watching = forms.ModelChoiceField(label=labels["watching"], queryset=Watching.objects.all())
	issuer = forms.ModelChoiceField(label=labels["issuer"], queryset=Issuer.objects.all())
	brigade = forms.ModelChoiceField(label=labels["brigade"], queryset=Member.objects.all())
	errand = forms.CharField(label=labels["errand"], max_length=512)
	add_instrs = forms.CharField(label=labels["add_instrs"], max_length=512)
	extrad_time = forms.DateTimeInput()
	start_time = forms.DateTimeInput()
	end_time = forms.DateTimeInput()
	installation_name = forms.CharField(label=labels["interventions"]["installation_name"], max_length=512)
	disconnections = forms.CharField(label=labels["interventions"]["disconnections"], max_length=512)
	protections = forms.CharField(label=labels["interventions"]["protections"], max_length=512)
