from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User",
        through="Follow",
        through_fields=("following_user", "followed_user"),
        related_name="followers",
    )

class Follow(models.Model):
    following_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_from"
    )
    followed_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_to"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="blogs")
    title = models.TextField(
        validators=[MinValueValidator(2), MaxValueValidator(280)],
    )
    description = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="blogs")
