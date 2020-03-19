from django.db import models

# Create your models here.
class Chords(models.Model):
    key = models.CharField(max_length=100, blank=False, default='C', null=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.key
