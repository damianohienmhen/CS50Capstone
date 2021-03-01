from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class User(AbstractUser):
    picture = models.ImageField(upload_to ='images', default="")
  
  
def serialize(self):
    return {
        "id": self.id,
        "name": self.username,
        }
 

class Business(models.Model):
    CATEGORIES = (
           ('Retail', 'Retail'),
           ('Utilities', 'Utilities'),
           ('Insurance', 'Insurance'),
           ('Transportation', 'Transportation'),
           ('Heatlh Care', 'Heatlh Care'),
           ('Internet', 'Internet'),
           ('Lodging & Travel', 'Lodging & Travel'),
           ('Sports & Recreation', 'Sports & Recreation'),
           ('Other', 'Other')
    )
    business_name = models.CharField(max_length=64, default="")
    image = models.ImageField(upload_to ='images', default="")
    description = models.CharField(max_length=64, default="")
    category = models.CharField(max_length=24, choices=CATEGORIES, default="" )
    date_posted = models.DateTimeField(auto_now_add=True, null= True, blank=True) 
    rating = models.ManyToManyField(User, related_name='raters', through='Rating')
  
    def serialize(self):
        return {
            "category": self.category.value()}
    def __str__(self):
        return f"{self.business_name}"
            

class RegisteredBusiness(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    thebusiness = models.ForeignKey(Business, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.owner} owns ({self.thebusiness})"
     
class Comment(models.Model):
    commentuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', default="")
    businessname= models.ForeignKey(Business, on_delete=models.CASCADE, related_name='businessname')
    new_comment= models.TextField()
    
    def serialize(self):
        return {
            "new_comment": self.new_comment,
            "id": self.id,
      }
    
    def __str__(self):
        return f"{self.commentuser} ({self.new_comment})"   

class Rating(models.Model):
    ratinguser =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratinguser', default="")
    business= models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    
    def __str__(self):
        return f"{self.ratinguser} rated {self.business} a {self.rating}"  
