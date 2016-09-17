from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class COne(models.Model):
    cid = models.CharField('CustomerID',max_length=50)
    uid = models.ForeignKey(User)
