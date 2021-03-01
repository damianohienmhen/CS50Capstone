from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newbusiness", views.newbusiness, name = "newbusiness"),
    path("registerbusiness", views.registerbusiness, name="registerbusiness"),
    path("businesslistings", views.businesslistings, name="businesslistings"),
    path("profilepage/<str:user>", views.profilepage, name = "profilepage"),
    path("category/<str:category>", views.eachcategory, name = "eachcategory"),
    path("business/<str:businessname>", views.businesspage, name = "businesspage"),
    path("create_comment/<str:businessname>", views.create_comment, name="create_comment"),
    path("rate_busines/<str:businessname>", views.rate_business, name="rate_business"),
    path("average/<str:business>", views.avgrating, name="average"),
    path("edit/<int:id>", views.edit, name = "edit"),
    path("submit/<int:id>", views.submit, name = "submit")

   
]