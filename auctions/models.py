
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=64, default="Fire")
    imgUrl = models.CharField(max_length=1000, default=False)

    def __str__(self):
        return f"{self.category_name}" 



class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=150)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_list")
    imageUrl = models.CharField(max_length=1000, default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=False)
    is_active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watch_list")

    def __str__(self):
        return self.title

class Bid(models.Model):
    bid = models.FloatField(default=None)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="itemBid")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBid")
    def __str__(self):
        return str(self.bid)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment", default=False)
    item = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="item_comment")
    message = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.message} by {self.author}"

