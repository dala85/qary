from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from qary_post import views

app_name = 'qary_post'


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.PostDetailView.as_view(), name='detail'),

]
