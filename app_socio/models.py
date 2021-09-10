from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userlist(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class userpost(models.Model):
    sno = models.AutoField(primary_key=True)
    lovers = models.ManyToManyField(User,related_name='lovers')
    likes = models.IntegerField(default=0)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='maker')

    def __str__(self):
        return self.user.username