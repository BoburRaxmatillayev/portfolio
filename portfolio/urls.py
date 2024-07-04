from django.urls import path
from .views import HomeView,article_detail
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('<int:id>/',views.article_detail,name="article-detail"),
]   