from django.db import models

class MettEater(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Metting(models.Model):
    organizer = models.ForeignKey(MettEater, related_name='organized_mettings')
    eaters = models.ManyToManyField(MettEater)
    date = models.DateField()

    def __str__(self):
        return '%s' % self.date
