from django.db import models

# Create your models here.
class place(models.Model):         #place is table name
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descrptn=models.TextField()

    def __str__(self):
        return self.name

class members(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name1



