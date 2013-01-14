from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^doquiz/$', 'quiz.views.doquiz'),
    url(r'^newquestion/$', 'quiz.views.newquestion'),
    url(r'^answer/(?P<question_id>\d+)/$', 'quiz.views.answer'),
    url(r'^dispute/(?P<question_id>\d+)/$', 'quiz.views.dispute'),
)

