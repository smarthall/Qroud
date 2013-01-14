from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'quiz.views.index'),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'quiz_login.html'}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
