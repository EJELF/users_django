from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

    @staticmethod
    def get_absolute_url():
        from django.urls import reverse
        return reverse('users')


