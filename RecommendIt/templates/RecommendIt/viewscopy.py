from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Model
import json
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.conf import settings # new
from django.http.response import JsonResponse

from .models import User, Business, RegisteredBusiness, Comment, Rating
from .forms import NewBusiness, CommentForm, RatingForm
# Create your views here.

def index(request):
    return render(request, "RecommendIt/homepage.html")
    
def profilepage(request, user):
    theuser = User.objects.get(username = user)
    ownedbusiness = RegisteredBusiness.objects.filter(owner = theuser)
    return render(request, "RecommendIt/myprofilepage.html", {
    "theuser": theuser, "ownedbusiness": ownedbusiness
    })


def newbusiness(request):
    cf = NewBusiness(request.POST or request.FILES or None) 
    return render(request, "RecommendIt/newbusiness.html", {
    "newbusiness": cf
    })

     
def businesslistings(request):
    return render(request, "RecommendIt/businesslistings.html", {
        "businesslistings": Business.objects.values('category').distinct()
        })

def eachcategory(request, category):
    categoryname = category
    businesslist = Business.objects.filter(category = category)
    return render(request, "RecommendIt/eachcategory.html", {
    "businesslist": businesslist, "categoryname": categoryname
    })
    
@login_required  
def businesspage(request, businessname):
    cf = CommentForm(request.POST or None) 
    rf = RatingForm(request.POST or None) 
    
    business = Business.objects.get(business_name = businessname)
    businessposts = Comment.objects.filter(businessname = business)
    paginator = Paginator(businessposts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    try:
        ratingobj = Rating.objects.get(business = business)
        ratings = ratingobj.rating
        if ratings in range(11):
            return render(request, "RecommendIt/businesspage.html", {
            "business": business,  "comment_form": cf, "page_obj": page_obj, "rating": ratings, 
            })
        
        else:
            return render(request, "RecommendIt/businesspage.html", {
            "business": business,  "comment_form": cf, "page_obj": page_obj, "rating_form": rf,
            })
    except:
        return render(request, "RecommendIt/businesspage.html", {
            "business": business,  "comment_form": cf, "page_obj": page_obj, "rating_form": rf,
            })
        
def create_comment(request, businessname): 
    if request.method == 'POST':
        businessname = Business.objects.get(business_name = businessname)
          
        businessposts = Comment.objects.filter(businessname = businessname)
        paginator = Paginator(businessposts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) 
        
        cf = CommentForm(request.POST or None) 
        if cf.is_valid(): 
            new_comment = request.POST.get('new_comment') 
            comment = Comment.objects.create(businessname = businessname, commentuser = request.user, new_comment = new_comment) 
            comment.save() 
            cf = CommentForm()
            
            ratingobj = Rating.objects.get(business = businessname)
            ratings = ratingobj.rating
            
            return render(request, "RecommendIt/businesspage.html", {
          "business": businessname,  "comment_form": cf, "page_obj": page_obj, "rating":ratings
            })
        
    else: 
        cf = CommentForm() 
        context ={'comment_form':cf} 
        
        businessname = Business.objects.get(business_name = businessname)
        businessposts = Comment.objects.filter(businessname = businessname)
        paginator = Paginator(businessposts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        ratingobj = Rating.objects.get(business = businessname)
        ratings = ratingobj.rating
        return render(request, "RecommendIt/businesspage.html", {
          "business": businessname,  "comment_form": cf, "page_obj": page_obj, "rating": ratings
            })


def rate_business(request, businessname): 
    if request.method == 'POST':
        businessname = Business.objects.get(business_name = businessname)
        businessposts = Comment.objects.filter(businessname = businessname)
        paginator = Paginator(businessposts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) 
        
        cf = CommentForm(request.POST or None) 
        rf = RatingForm(request.POST or None) 
        if rf.is_valid(): 
            rating = request.POST.get('rating')
            
            rating = Rating.objects.create(business = businessname, ratinguser = request.user, rating = rating) 
            rating.save() 
            cf = CommentForm()
            rf = RatingForm()
        return render(request, "RecommendIt/homepage.html", {
        "rate": ('Thank you for rating %s' %businessname),  "comment_form": cf, "page_obj": page_obj, "rating_form": rf,
           })
        
        
    else: 
        rf = RatingForm() 
        context ={'rating_form':rf} 
        cf = CommentForm(request.POST or None) 
        businessname = Business.objects.get(business_name = businessname)
        businessposts = Comment.objects.filter(businessname = businessname)
        paginator = Paginator(businessposts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) 
        
        cf = CommentForm()
        return render(request, "RecommendIt/businesspage.html", {
        "business": businessname,  "comment_form": cf, "page_obj": page_obj, "rating_form": rf,
        })
        

def newbusiness(request):
    cf = NewBusiness(request.POST or request.FILES or None) 
    return render(request, "RecommendIt/newbusiness.html", {
    "newbusiness": cf
    })
    
def registerbusiness(request):
    if request.method == 'POST' or request.method =="FILES":
        theuser = request.user
        business_name = request.POST.get('business_name') 
        posteduser = request.POST.get(theuser)
        description = request.POST.get('description')
        image= request.FILES.get('image')
        category=request.POST.get('category')
        newbusiness = Business.objects.create(business_name = business_name, description = description, image =  image, category=category) 
        newbusiness.save()
     
        regbusiness = RegisteredBusiness.objects.create(owner = theuser, thebusiness = newbusiness)
      
        return render(request, "RecommendIt/homepage.html" , {
                "message": "You've Succesfully Registered Your Business!"
            })
    
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "RecommendIt/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "RecommendIt/login.html")
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

    
def register(request):
    if request.method == "POST" or request.method == "FILES":
        image = request.FILES['image']
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "RecommendIt/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create(username = username, email = email, password =  password, picture = image) 
            user.save()
       
        except IntegrityError:
            return render(request, "RecommendIt/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "RecommendIt/register.html")
