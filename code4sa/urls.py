from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', view=lambda r: HttpResponse("Hello :)", content_type="text/plain")),

    url(r'^token/$', 'code4sa.views.token'),
    url(r'^submit/taxtool/$', 'code4sa.views.submit', kwargs={'project': 'taxtool'}),

    url(r'^admin/', include(admin.site.urls)),
)
