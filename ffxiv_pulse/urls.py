from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'content.views.index', name='index'),
    url(r'^news/(?P<news_id>\d+)', 'content.views.news', name='news'),
    url(r'^admin/', include(admin.site.urls)),
)
