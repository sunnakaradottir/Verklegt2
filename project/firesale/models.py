from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyData(models.Model):
    # Testing model
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Member(models.Model):
    image = models.ForeignKey('MemberImage', on_delete=models.CASCADE, blank=True, null=True, related_name='profile_picture')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=7)
    birthday = models.DateField()
    bio = models.CharField(max_length=1000, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"

class MemberImage(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='member', null=True)
    img_url = models.CharField(max_length=1000)

class ItemImage(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='item', null=True)
    img_url = models.CharField(max_length=1000)

class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ForeignKey('ItemImage', on_delete=models.CASCADE, blank=True, null=True, related_name='item_image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_location = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item name: {self.name}, id: {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField()

class Bid(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class Message(models.Model):
    sender = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('read', 'Read'),
        ('unread', 'Unread'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unread')

class Order(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='orders_as_buyer')
    seller = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='orders_as_seller')
    amount = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')

class Review(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    from_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='reviews_sent')
    to_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='reviews_recieved')
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='my_favorites')
    creation_time = models.DateTimeField(auto_now_add=True)