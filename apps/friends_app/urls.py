from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='friends-page'),
    url(r'^(?P<id>\d+)$', views.person, name='person'),
    url(r'^add/(?P<id>\d+)$', views.addFriend, name='add-friend'),
    url(r'^remove/(?P<id>\d+)$', views.removeFriend, name='remove-friend'),
    url(r'^', views.index, name='leftover'),
]
