from django.contrib import admin

# Register your models here.

from .models import User, Business, RegisteredBusiness, Rating, Comment

admin.site.register(User)
admin.site.register(Business)
admin.site.register(RegisteredBusiness)
admin.site.register(Comment)
admin.site.register(Rating)