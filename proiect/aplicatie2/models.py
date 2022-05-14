from django.db import models


class Movies(models.Model):

    title = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    added = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.type} - {self.rating}"
