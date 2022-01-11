from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    department = models.CharField(max_length=60)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
