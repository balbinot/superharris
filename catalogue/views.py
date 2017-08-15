from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from catalogue.models import GlobularCluster, AllObservation, Reference
import django_tables2 as tables
from django.shortcuts import get_object_or_404, render

class ObservationTable(tables.Table):
    class Meta:
        model = AllObservation
        exclude = ('id', 'cluster_id')

class ReferenceTable(tables.Table):
    class Meta:
        model = Reference
        exclude = ('id',)

class CoordinateTable(tables.Table):
    class Meta:
        model = AllObservation
        fields = ('cluster_id', 'ra', 'dec', 'gallon', 'gallat', 'dfs', 'dfgc', 'gc_x', 'gc_y', 'gc_z')

class MetallicityTable(tables.Table):
    class Meta:
        model = AllObservation
        fields = ('cluster_id', 'metallicity', 'w_mean_met', 'FG_red', 'V_horiz', 'app_dist', 'Int_V_mag', 'm_v_t', 'ph_u_b', 'ph_b_v', 'ph_b_v', 'ph_v_r', 'ph_v_i', 'spec_type', 'ellipticity')

class OtherTable(tables.Table):
    class Meta:
        model = AllObservation
        exclude = ('id', 'ref', 'metallicity', 'w_mean_met', 'FG_red', 'V_horiz', 'app_dist', 'Int_V_mag', 'm_v_t', 'ph_u_b', 'ph_b_v', 'ph_b_v', 'ph_v_r', 'ph_v_i', 'spec_type', 'ellipticity', 'ra', 'dec', 'gallon', 'gallat', 'dfs', 'dfgc', 'gc_x', 'gc_y', 'gc_z', 'name')


def index(request):
    return render(request, 'index.html', {'observations': AllObservation.objects.all()})


def references(request):
    table = ReferenceTable(Reference.objects.all())
    return render(request, 'references.html', {'references': table})


def detail(request, cluster_id_id):
    cluster = get_object_or_404(GlobularCluster, pk=cluster_id_id)
    table = ObservationTable(AllObservation.objects.filter(cluster_id=cluster))
    return render(request, 'detail.html', {'observations': table, 'cluster' : cluster})


def Harris_2010_coordinates(request):
     reference =  get_object_or_404(Reference, pk=2)
     table = CoordinateTable(AllObservation.objects.filter(ref=reference))
     return render(request, 'view1.html', {'coordinates': table})

def Harris_2010_metallicity(request):
     reference =  get_object_or_404(Reference, pk=2)
     table = MetallicityTable(AllObservation.objects.filter(ref=reference))
     return render(request, 'view2.html', {'metallicity' : table})

def Harris_2010_velocities(request):
     reference =  get_object_or_404(Reference, pk=2)
     table = OtherTable(AllObservation.objects.filter(ref=reference))
     return render(request, 'view3.html', {'velocities' : table})
