from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^$', views.index, name='register1'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
]
