from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email=models.EmailField(default="abc@gmail.com")
    password = models.CharField(max_length=30)
