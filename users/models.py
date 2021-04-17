from django.db import models


class User(models.Model):
    username = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.username} {self.email}"

