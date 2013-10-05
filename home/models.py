from django.db import models

class Dude(models.Model):
    name = models.CharField(max_length=256)

class Vote(models.Model):
    dude = models.ForeignKey(Dude)
    pants = models.IntegerField(default=True)
    ip = models.CharField(max_length=256)


class Comment(models.Model):
    name = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)
    tstamp = models.DateTimeField(auto_now_add=True)
