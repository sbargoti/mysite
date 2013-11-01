from django.contrib import admin
from vehicle.models import Car
from production.models import Manufacturer

class ManufacturerInLine(admin.TabularInline):
    model = Manufacturer
    extra = 3

class CarAdmin(admin.ModelAdmin):
    fields = ['nickname','year','manufacturer']

admin.site.register(Car,CarAdmin)
