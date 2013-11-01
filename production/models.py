from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField('Manufacturer Name',max_length = 255)

    def __unicode__(self):
        return self.name
    
    def ManCars(self):
        return self.car_set.all()
