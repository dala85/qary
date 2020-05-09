from django.conf.urls import url
from qary_post import views

app_name = 'qary_post'


urlpatterns = [

    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^new/$', views.PostCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name='delete'),
]
