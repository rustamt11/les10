from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}-{self.surname}"

    def get_absolut_url(self):
        return f"/check/{self.pk}"
