from django.db import models
from supers.models import Super

# Create your models here.

class SuperType(models.Model):
    type = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    super_type = models.ForeignKey(Super, on_delete=models.CASCADE, null=True)




# type Charfield