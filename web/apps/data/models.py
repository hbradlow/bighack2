from django.db import models

class Appliance(models.Model):
	name = models.CharField(max_length=50) #example field
