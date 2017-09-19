from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^GCID(?P<cluster_id_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^references/(?P<name_id>[0-9]+)/$', views.ref_detail, name='ref_detail'),
    url(r'^references/$', views.references, name='references'),
    url(r'^Coordinates_harris2010/$', views.Harris_2010_coordinates, name='Harris_2010_coordinates'),
    url(r'^Metallicity_harris2010/$', views.Harris_2010_metallicity, name='Harris_2010_metallicity'),
    url(r'^Velocities_harris2010/$', views.Harris_2010_velocities, name='Harris_2010_velocities'),
]
