from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    username=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=150)
    birthday=models.DateField(null=True,blank=True)
    personal_img=models.ImageField(upload_to="PersonalImages/",null=True,blank=True)

    def __str__(self):
        return self.username

class Video(models.Model):
    title=models.CharField(max_length=255)
    category=models.CharField(max_length=100)
    video_url=models.FileField(upload_to=f"Vedios/")
    description=models.CharField(max_length=510)
    tag1=models.CharField(max_length=100)
    tag2=models.CharField(max_length=100)
    tag3=models.CharField(max_length=100)
    love=models.IntegerField(default=0,null=True,blank=True)
    comment=models.IntegerField(default=0,null=True,blank=True)
    share=models.IntegerField(default=0,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

class UserInfo(models.Model):
    following=models.IntegerField(null=True,blank=True)
    followers=models.IntegerField(null=True,blank=True)
    likes=models.IntegerField(null=True,blank=True)
    videos=models.ForeignKey(Video,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class UserInterests(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)




















