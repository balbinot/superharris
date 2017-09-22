from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^GCID(?P<cluster_id_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^references/$', views.references, name='references'),
    url(r'^view1/$', views.view1, name='view1'),
    url(r'^view2/$', views.view2, name='view2'),
    url(r'^view3/$', views.view3, name='view3'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registered/$', views.registered, name='registered'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^submitted/$', views.submitted, name='submitted'),
    url(r'^account/$', views.user_account, name='account'),
]
