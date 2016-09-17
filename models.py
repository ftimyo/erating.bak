from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bank(models.Model):
    uid = models.ForeignKey(User)
    cid = models.CharField('CustomerID',max_length=50)
