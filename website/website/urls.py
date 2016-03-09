from django.conf.urls import url, include
from django.contrib import admin
from voting import urls as voting_urls
from blog import urls as blog_urls
from django.contrib.auth.views import login, logout

urlpatterns = [url(r'^', include(blog_urls)),
               url(r'^vote/', include(voting_urls)),
               url(r'^admin/', admin.site.urls),
               url(r'^login/$', login,
                   name='login', kwargs={'template_name': 'login.html', }
                   ),
               url(r'^logout/$', logout,
                   name='logout', kwargs={'next_page': '/'}
                   ),
]
