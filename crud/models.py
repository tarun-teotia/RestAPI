from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)

class Item2(models.Model):
    tasks = []