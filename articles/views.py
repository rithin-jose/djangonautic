from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.object.all().order_by('date') 
    return render(request, 'articles/article_list.html',{'articles':articles})