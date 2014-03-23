from django.shortcuts import render
from content.models import *

# Create your views here.
def index(request):
    recent_news = News.objects.all()
    context = {'news': recent_news}
    return render(request, 'index.html', context)
