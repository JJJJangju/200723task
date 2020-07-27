from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# user model 과 1:1 의 관계임을 나타냄
	nickname = models.CharField(max_length=50)
	region = models.CharField(max_length=50)