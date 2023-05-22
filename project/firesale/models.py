from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyData(models.Model):
    # Testing model
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Member(models.Model):
    image_id = models.ForeignKey('MemberImage', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=7)
    birthday = models.DateField()
    bio = models.CharField(max_length=1000, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"

class MemberImage(models.Model):
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='profile_picture')
    img_url = models.CharField(max_length=1000)

class ItemImage(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='item_image')
    img_url = models.CharField(max_length=1000)

class Item(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    image_id = models.ForeignKey('ItemImage', on_delete=models.CASCADE, blank=True, null=True)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='my_listings')
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)
    bid_id = models.ForeignKey('Bid', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True) # AFH ÞURFTI ÉG AÐ GERA BLANK=TRUE OG NULL = TRUE
    condition = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item name: {self.name}, id: {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField()

class Bid(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='bids')
    bid_amount = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class Message(models.Model):
    sender_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='sent_messages')
    receiver_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('read', 'Read'),
        ('unread', 'Unread'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unread')

class Order(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='orders_as_buyer')
    seller_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='orders_as_seller')
    bid_id = models.ForeignKey('Bid', on_delete=models.CASCADE)
    amount = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')

class Review(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    from_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='reviews_sent')
    to_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='reviews_recieved')
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='my_favorites')
    creation_time = models.DateTimeField(auto_now_add=True)