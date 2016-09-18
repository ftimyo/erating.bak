from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bank(models.Model):
    uid = models.ForeignKey(User)
    cid = models.CharField('CustomerID',max_length=50)
class GreenMerchants(models.Model):
    mid = models.CharField('MerchantID',max_length=50)
    mname = models.CharField('MerchantName',max_length=100)
    mcat = models.TextField('MerchantCatagories')
    mreward = models.FloatField("Reward")

    def __str__(self):
        return self.mname
    class Meta:
        ordering = ('mname',)
