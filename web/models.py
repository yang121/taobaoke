from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(verbose_name='商品名称', max_length=128, unique=True, null=True, blank=True)
