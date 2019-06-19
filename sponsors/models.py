from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name                                           = models.CharField(max_length=100)
    #organizers                                     = models.ManyToManyField('Organizer', blank = True)
    contacted_regarding_event                      = models.BooleanField()
    confirmed_sponsor                              = models.BooleanField()
    prospective_sponsors                           = models.BooleanField()
    #delete above
    #can get events sponsored through querysets

    def __str__(self):
        return self.name
