from django.db import models

# Create your models here.
class ConsumerModel(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)