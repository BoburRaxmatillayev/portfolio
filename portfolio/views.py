from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import CommentForm
from .bot import send_message
from .models import Article, Contact,Comment #, Portfolio
from django.views.generic import View

class HomeView(View):
    template_name = "index.html"
    
    
    
    def get(self, request, *args, **kwargs):
        articles=Article.objects.all()
        context = {
        "articles": articles,
        #"portfolios": portfolios,
    }
        return render(request, self.template_name,context=context)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(name=name,email=email,description=message)
        contact.save()
        print("SALOM")
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('home-page'))   


def article_detail(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
          first_name = form.data.get("first_name")
          text = form.data["text"]
          rating = form.data["rating"]
          comment = Comment(
            first_name = first_name,
            text = text,
            rating = rating,
            article = article,
          )
          comment.save()
          messages.success(request,'Izoh yuborildi')
          return HttpResponseRedirect(reverse("article-detail",args=[id]))


    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id).order_by("-create_date")
    
    form = CommentForm()
    context = {"article":article,"comments":comments, "form":form}
    return render(request,"article.html",context)
