from django.db import models

# Create your models here.
class LoginModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class MarchentModel(models.Model):
    mrt_id = models.IntegerField(primary_key=True,default=False)
    mrt_name = models.CharField(max_length=30)
    Email_id = models.EmailField()
    contactNo = models.CharField(max_length=10)
    password=models.CharField(max_length=10,default=False)



class ProductModel(models.Model):
    p_no = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=30)
    p_price = models.FloatField()
    p_quantity = models.IntegerField()
    m_id = models.ForeignKey(MarchentModel,on_delete=models.CASCADE)