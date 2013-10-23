from django.db import models

# Create your models here.
class Car(models.Model):
    manufacturer = models.ManyToManyField('production.Manufacturer')
    nickname = models.CharField(max_length = 255)
    year = models.IntegerField(default = 2010)

    def __unicode__(self):
        return self.nickname
