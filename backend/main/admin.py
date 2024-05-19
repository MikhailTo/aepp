from django.contrib import admin
from .models import Manuals, Categories, Groups

admin.site.site_header = "Панель администрирования"

# Register your models here.
admin.site.register(Manuals)
admin.site.register(Groups)
admin.site.register(Categories)