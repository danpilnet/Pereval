from django.db import models


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

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)