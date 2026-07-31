from django.db import models
from django.core.validators import MinValueValidator,RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Farm(models.Model):
    name=models.CharField(max_length=20,verbose_name="name")
    city=models.CharField(max_length=30,verbose_name="city")
    area=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="مساحت")
    descreaption=models.TextField(verbose_name="description")
    phone=models.CharField(max_length=11,validators=[
        RegexValidator(
            regex=r'^0\d{10}$',  # 0 + 10 رقم
            message='The phone number must start with 0 and be 11 digits long.'
        )
    ]
    ,verbose_name='phone number')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name