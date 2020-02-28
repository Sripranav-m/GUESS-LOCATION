from django.db import models

from django.db import models

class userdata(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class carousel_Image(models.Model):
    username=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return (self.username+"->"+self.name)


class points(models.Model):
    username=models.CharField(max_length=100,default="")
    point=models.IntegerField(default=0)
    q_ans=models.CharField(max_length=1000,default="")
    def __str__(self):
        return (self.username+"->")