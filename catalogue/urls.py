from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^GCID(?P<cluster_id_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^references/$', views.references, name='references'),
]
