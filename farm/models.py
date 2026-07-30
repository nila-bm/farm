from django.db import models
from django.core.validators import MinValueValidator,RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Farm(models.Model):
    name=models.CharField(max_length=20,verbose_name="نام")
    city=models.CharField(max_length=30,verbose_name="شهر")
    area=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="مساحت")
    descreaption=models.TextField(verbose_name="توضیحات")
    phone=models.CharField(max_length=11,validators=[
        RegexValidator(
            regex=r'^0\d{10}$',  # 0 + 10 رقم
            message='شماره تلفن باید با 0 شروع شود و 11 رقم باشد'
        )
    ]
    ,verbose_name='شماره موبایل')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name