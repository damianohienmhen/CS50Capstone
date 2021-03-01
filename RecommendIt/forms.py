from .models import Business, Comment, Rating, Business
from django import forms



class NewBusiness(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['business_name', 'category', 'description', 'image']
        

class CommentForm(forms.ModelForm):
    new_comment = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':4, 
        'cols':50}))

    class Meta:
        model = Comment
        fields = ['new_comment']
        


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['rating']


    