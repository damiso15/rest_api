from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name
