from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator

labels = {
        "date":   "Дата настройки",
        "winder":   "Моталка №",
        "roll":     "Формирующий ролик",
		"task":		"Задание с клином в привод, %",
		"cspd": 	"Корректировка фактической скорости",
		"tspd":		"Выставленная скорость по заданию, м/с",
		"fspd":		"Фактическая скорость на терминале, м/с",
		"bmav":		"Изм. угл. факт. скорость до корр., об/мин",
		"bemf":		"Значение параметра P115.2 до изменения",
		"amav":		"Изм. угл. факт. скорость после корр., об/мин",
		"aemf":		"Значение параметра P115.2 после изменения",
		"dtmav":	"Разница скоростей заданной от фактической, %",
		"corr": 	"Корректировка скоростей",
	}

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Speed(models.Model):
    date = models.DateField(verbose_name=labels['date'])
    winder = models.IntegerField(blank=False, verbose_name=labels['winder'])
    roll = models.IntegerField(blank=False, verbose_name=labels['roll'])
    task = models.FloatField(blank=False, verbose_name=labels['task'])
    cspd = models.BooleanField(default=False, verbose_name=labels['cspd'])
    tspd = models.FloatField(default=10.0, verbose_name=labels['tspd'])
    bmav = models.IntegerField(blank=False, verbose_name=labels['bmav'])
    bemf = models.FloatField(blank=False, verbose_name=labels['bemf'])
    amav = models.IntegerField(blank=False, verbose_name=labels['amav'])
    aemf = models.FloatField(blank=False, verbose_name=labels['aemf'])
    corr = models.BooleanField(default=True, verbose_name=labels['corr'])

    def __str__(self):
        return 'Моталка №' + self.winder + ' (' + self.date + ')'
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    aggregate = models.CharField(max_length=100)
    cabinet = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name + ' -> ' + self.type + ' -> ' + self.aggregate


class Location(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=False)
    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=False)
    color = models.CharField(max_length=255, default='grey')
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=128)

    def __str__(self):
        return self.company_name


class Division(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=False, default=0)
    division_name = models.CharField(max_length=128)

    def __str__(self):
        return self.division_name


class Group(models.Model):
    division = models.ForeignKey('Division', on_delete=models.CASCADE, null=False, default=0)
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name

class Order(models.Model):
    order_number = models.IntegerField(default="")
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=False, default=0)
    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=False, default=0)
    issuer = models.ForeignKey('Issuer', on_delete=models.PROTECT, null=False)
    accountable_name = models.CharField(max_length=128, default="Не назначается")
    allower_name = models.CharField(max_length=128, default="оперативному персоналу")
    producer = models.ForeignKey('Member', on_delete=models.PROTECT, null=False)
    watching = models.ForeignKey('Watching', on_delete=models.PROTECT, null=False, default=0)
    brigade = models.ForeignKey('Brigade', on_delete=models.PROTECT, null=False)
    errand = models.CharField(max_length=512)
    add_instrs = models.CharField(max_length=512)
    extrad_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    interventions = models.ForeignKey('Interventions', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.errand


class Interventions(models.Model):
    installation_name = models.CharField(max_length=255)
    disconnections = models.CharField(max_length=255)
    protections = models.CharField(max_length=255, default="Не требуется")

    def __str__(self):
        return self.installation_name + ': ' + self.disconnections


class Watching(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Issuer(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Member(models.Model):
    full_name = models.CharField(max_length=128)
    access_group = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name + ' ' + self.access_group + 'гр.'


class Brigade(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Member, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE)

class Companies(models.Model):

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('images', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=512, blank=True,)
    image = models.FileField(upload_to="media/products/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                              validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    link = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title
    
class Categories(models.Model):
    class Meta:
        verbose_name = 'Категории инструкций'
        verbose_name_plural = 'Категории инструкций'

    name = models.CharField(max_length=128, verbose_name="Наименование категории", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    
    def __str__(self):
        return self.name + '(' + self.slug + ')'
    
class Groups(models.Model):
    class Meta:
        verbose_name = 'Группа инструкций'
        verbose_name_plural = 'Группа инструкций'
    
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория", blank=True)
    name = models.CharField(max_length=128, verbose_name="Группа инструкций", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    
    def __str__(self):
        return self.name + '(' + self.slug + ')'
    

class Manuals(models.Model):
    class Meta:
        verbose_name = 'Инструкции'
        verbose_name_plural = 'Инструкции'
    
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория", blank=True)
    group = models.ForeignKey('Groups', on_delete=models.PROTECT, null=True, verbose_name="Группа", blank=True)
    name = models.CharField(max_length=128, verbose_name="Наименование инструкции", blank=True)
    image = models.ImageField(verbose_name="Картинка инструкции",
                                upload_to="manuals/",
                                default='/static/images/default/no-image.svg',
                                null=True,
                                blank=True,
                                storage=FileSystemStorage(location=str(settings.BASE_DIR), base_url='/'),
                                validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'webp'])])
    # link = models.FileField(upload_to="manuals/",
    #                           null=True,
    #                           blank=False,
    #                           validators=[FileExtensionValidator(['pdf'])])                            
    # link = models.CharField(max_length=128, verbose_name="Ссылка каталога", blank=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.group) + ')'