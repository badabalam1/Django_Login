from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^accounts/login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^accounts/signup/$', views.CreateUserView.as_view(), name='signup'),
    url(r'^accounts/login/done$',
        views.ResisteredView.as_view(), name='create_user_done')
]
