from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', view=lambda r: HttpResponse("Hello :)", content_type="text/plain")),

    url(r'^submit/budget2016/$', 'code4sa.views.submit', kwargs={'project': 'budget2016'}),
    url(r'^submit/budget2016/notice$', 'code4sa.views.budget2016_notice'),

    url(r'^admin/', include(admin.site.urls)),
)
