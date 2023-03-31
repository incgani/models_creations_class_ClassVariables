from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100)

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()

class AccessRecords(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

