from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from pants.home.feeds import *

urlpatterns = patterns(
    'pants.home.views',
    (r'^/$', 'index'),
    (r'^$', 'index'),
    (r'^about/', TemplateView.as_view(template_name="about.html")),
    (r'^(\d+)/$', 'getvote'),
    (r'^addvote/$', 'addvote'),
    (r'^adddude/$', 'adddude'),
    (r'^comment/', TemplateView.as_view(template_name="comment.html")),
    (r'^addcomment/$', 'addcomment'),
    (r'^comments/$', 'comments'),  
    (r'^rss/$', LatestFeed())

)
