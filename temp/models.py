from django.db import models

# Create your models here.

class TempModel(models.Model):
    time = models.DateTimeField("time", auto_now_add=True)
    tempValue = models.IntegerField("tempValue")
    date = models.DateField("date", auto_now_add=True)


    def __str__(self):
        return self.tempValue
    