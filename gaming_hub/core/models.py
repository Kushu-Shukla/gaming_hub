from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='game_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

