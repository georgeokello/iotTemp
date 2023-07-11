from django.db import models

# Create your models here.

class TempModel(models.Model):
    time = models.DateTimeField("time", auto_now_add=True)
    tempValue = models.IntegerField("tempValue")
    
    def __str__(self):
        return str(self.tempValue)
    