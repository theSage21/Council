from django.conf.urls import url
from voting import views

urlpatterns = [url(r'^$', views.home, name='vote_home'),
               url(r'^(?P<tid>\d+)/$', views.topic, name='topic'),
]
