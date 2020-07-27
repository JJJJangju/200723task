from django.db import models
from django.contrib.auth.models import User

class Blogapp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #ForeignKey 처음에는 참조할 모델, 그 모델이 사라졌을 때 delete사용  
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]    