from django.db import models
from django.contrib.auth.models import User


#Tranier
class Article(models.Model):
    # author = models.ForeignKey(User,on_delete=models.CASCADE)

    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    # description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    # create_data = models.DateTimeField(auto_now=True)
    #4ta maydon qo'shish
    def __str__(self) -> str:
        return f"{self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    # phone_number = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField()

    article = models.ForeignKey(Article,on_delete=models.CASCADE)
# class Portfolio(models.Model):
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=200)
#     url_GitHub = models.URLField()
#     description = models.TextField()
#     is_active = models.BooleanField(default=False)
#     image = models.ImageField(upload_to="Portfolio/image")
#     create_data = models.DateTimeField(auto_now=True)
#     #4ta maydon qo'shish
    
#     def __str__(self) -> str:
#         return f"{self.title}"