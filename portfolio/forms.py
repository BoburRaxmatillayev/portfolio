from django.forms import ModelForm
from .models import Contact
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator 


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()

class CommentForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)
    # rating = forms.IntegerField(validators=[MinValueValidator(1),]) 