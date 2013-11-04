from django.db import models

# Create your models here.
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
