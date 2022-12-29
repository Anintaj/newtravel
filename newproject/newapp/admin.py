from django.contrib import admin

# Register your models here.
from . models import newdb
from . models import team
admin.site.register(newdb)
admin.site.register(team)


