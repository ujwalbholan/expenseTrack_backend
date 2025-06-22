from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    limit = models.FloatField()
    spent = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.category}"
