from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
