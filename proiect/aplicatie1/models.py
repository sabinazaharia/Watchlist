from django.db import models

score = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))


class Watchlist(models.Model):

    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    your_rating = models.IntegerField(choices=score, null=True)
    watched = models.BooleanField(default=0, null=True)

    def __str___(self):
        return f"{self.title} - {self.year} - {self.type} - {self.rating} - {self.your_rating}"
