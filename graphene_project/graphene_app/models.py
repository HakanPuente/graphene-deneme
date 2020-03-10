from django.db import models

class CardBoard(models.Model):
    label = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)