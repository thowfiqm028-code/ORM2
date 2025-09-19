from django.db import models
from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand = models.CharField()
    model = models.CharField()
    mfg_date = models.DateField()
    colour = models.CharField()
    fc = models.DateField()
    fuel_type = models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'mfg_date', 'colour', 'fc', 'fuel_type')
