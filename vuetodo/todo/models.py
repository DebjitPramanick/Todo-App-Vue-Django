from django.db import models

# Create your models here.

class Task(models.Model):
    TODO = 'Todo'
    DONE = 'Done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
