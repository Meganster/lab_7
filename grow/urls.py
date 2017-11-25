from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>(\d+))$', views.department, name='department'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login')
]