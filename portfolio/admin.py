from django.contrib import admin
from .models import Article, Contact,Comment#,Portfolio
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","image"]
    list_filter = ["is_active"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]