from django.db import models
from django.utils import timezone

class SearchRecord(models.Model):
    url = models.URLField()
    keywords = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)#time
    updated_at = models.DateTimeField(auto_now=True)#time of test
    count_of_matches = models.IntegerField(default=0)
    time_spent = models.CharField(max_length=255)
    def __str__(self):
        return self.url
