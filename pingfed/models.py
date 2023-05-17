from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(verbose_name="User name", max_length=255)
    email = models.EmailField(verbose_name="User email", max_length=255)

    def __str__(self):
        return f"{self.name}-{self.email}"