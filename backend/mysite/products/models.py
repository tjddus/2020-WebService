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
    publishedYn = models.BooleanField(default=0)
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
    grade = models.CharField(max_length=10)
    content = models.CharField(max_length=300)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents