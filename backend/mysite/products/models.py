from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    pid=models.IntegerField(null=False)
    name = models.CharField(null=True, default='', max_length=300)
    category = models.CharField(default='', max_length=30)
    makerName = models.CharField(null=True, default='', max_length=50)
    photoUrl = models.CharField(max_length=500)
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(null=True)
    achievementRate = models.IntegerField(default=0)
    totalAmount = models.IntegerField(default=0)
    totalSupporter = models.IntegerField(default=0)
    totalLike = models.IntegerField(default=0)
    endYn = models.BooleanField(default=False)
    detailUrl = models.CharField(max_length=500)
    class Meta:
        ordering = ['createdDate']

class Tester(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)