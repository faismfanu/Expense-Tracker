from django.db import models

# Create your models here.

# Created Model called Expense for tracking expense
class Expense(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"(self.name)"
