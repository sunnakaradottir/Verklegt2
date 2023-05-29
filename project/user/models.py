from django.db import models
from django.contrib.auth.models import User
from firesale.models import Item

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    favorite_item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True, related_name='favorite_item')
    profile_image = models.CharField(max_length=9999, blank=True, null=True)
    average_rating = models.DecimalField(decimal_places=1, default=0.0, max_digits=3)