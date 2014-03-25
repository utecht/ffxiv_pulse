from django.core.urlresolvers import reverse
from django.shortcuts import render
from content.models import *

# Create your views here.
def index(request):
    recent_news = News.objects.all().order_by('-publish_date')
    updates = []
    for u in News.objects.all():
        updates.append({'name':u.title,
                        'url':reverse('news', kwargs={'news_id':u.id}),
                        'date':u.publish_date})

    context = {'news': recent_news, 'updates':updates}
    return render(request, 'index.html', context)


def news(request, news_id):
    n = News.objects.get(id=news_id)
    context = {'n': n}
    return render(request, 'news.html', context)
