from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD", "Hard"
        SOFT = "SOFT", "Soft"
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices,
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
