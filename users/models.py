from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
