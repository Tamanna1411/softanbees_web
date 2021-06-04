
from django.db import models

# Create your models here.
class ApplyModel(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profession = models.CharField(max_length=50,null=True)
    

    def __str__(self):
        return self.name
 

