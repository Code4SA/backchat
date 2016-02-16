from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'code4sa.views.home', name='home'),

    url(r'/submit/taxtool/^$', 'code4sa.views.submit', kwargs={'project': 'taxtool'}),

    url(r'^admin/', include(admin.site.urls)),
)
