from django.db import models
from django.contrib import admin

class Appliance(models.Model):
    manufacturer = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    annual_energy_consumption = models.FloatField()

class Heater(models.Model):
    boiler_type = models.CharField(max_length=50)
    burner_type = models.CharField(max_length=50)
    energy_source = models.CharField(max_length=50)
    pilot_light = models.CharField(max_length=50)
    outdoor = models.BooleanField()
    flue_gas = models.CharField(max_length=50)
    control = models.CharField(max_length=50)
    boiler_design = models.CharField(max_length=50)
    appliance = models.ForeignKey(Appliance)
    
class Fridge(models.Model):
    appliance = models.ForeignKey(Appliance)
    style = models.CharField(max_length=50)
    defrost = models.CharField(max_length=50)
    fridge_type = models.CharField(max_length=50)
    access = models.CharField(max_length=50)
    fresh_volume = models.FloatField()
    freezer_volume = models.FloatField()
    total_volume = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    model = models.CharField(max_length=50)
    
admin.site.register(Appliance)
admin.site.register(Heater)
admin.site.register(Fridge)
