from django.db import models


class UserPereval(models.Model):
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pnone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)

class Status(models.Model):

    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'

    STATUS_CHOICES = [(NEW, 'New'),
                      (PENDING, 'Pending'),
                      (ACCEPTED, 'Accepted'),
                      (REJECTED, 'Rejected'),

    ]

    user = models.ForeignKey(UserPereval, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)

class Pereval(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(UserPereval, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)

class Coordinates(models.Model):
    longitude = models.DecimalField(max_digits=10, decimal_places=8, unique=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, unique=True)
    height = models.DecimalField(max_digits=10, decimal_places=8, unique=True)