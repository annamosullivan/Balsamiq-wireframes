from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT
from hello import views
from accounts.views import register, profile, login, logout, cancel_subscription


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
    url(r'^$', views.get_index),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^//logout/$', logout, name='logout'),
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
]