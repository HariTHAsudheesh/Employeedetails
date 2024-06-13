from django.db import models

# Create your models here.
class company(models.Model):
    cmpname=models.CharField(max_length=200,unique=True)
    empname=models.CharField(max_length=200)
    empQuali=models.CharField(max_length=200)
    empDept=models.CharField(max_length=200)
    empDsg=models.CharField(max_length=200)
    empImg=models.ImageField(upload_to='images',default="images/default.jpg",blank=True)
    empJdate=models.DateTimeField()
    empSalary=models.IntegerField()
    empPhone=models.IntegerField()

def __str__(self):
        return self.cmpname