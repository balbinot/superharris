from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from catalogue.models import GlobularCluster, AllObservation, Reference
import django_tables2 as tables
from django.shortcuts import get_object_or_404, render
from django_tables2.utils import A  # alias for Accessor

class ObservationTable(tables.Table):
    class Meta:
        model = AllObservation
        exclude = ('id', 'cluster_id')

class ReferenceTable(tables.Table):
    doi = tables.URLColumn()
    ads = tables.URLColumn()
    name = tables.LinkColumn('ref_detail', args=[A('pk')])
    pub_date = tables.DateColumn()
    class Meta:
        model = Reference
        exclude = ('id',)

class HarrisTable(tables.Table):
    cluster_id = tables.LinkColumn('detail', args=[A('pk')])
    reference =  get_object_or_404(Reference, pk=2)
    class Meta:
        model = AllObservation
        exclude = ('id', 'ref')

class GeneralTable(tables.Table):
    cluster_id = tables.LinkColumn('detail', args=[A('pk')])
    class Meta:
        model = AllObservation
        exclude = ('id', 'ref')

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
    reference =  get_object_or_404(Reference, pk=2)
    table = HarrisTable(AllObservation.objects.filter(ref=reference))
    return render(request, 'index.html', {'observations': table})


def references(request):
    table = ReferenceTable(Reference.objects.all())
    return render(request, 'references.html', {'references': table})

def detail(request, cluster_id_id):
    cluster = get_object_or_404(GlobularCluster, pk=cluster_id_id)
    table = ObservationTable(AllObservation.objects.filter(cluster_id=cluster))
    return render(request, 'detail.html', {'observations': table, 'cluster' : cluster})

def ref_detail(request, name_id):
    reference = get_object_or_404(Reference, pk=name_id)
    table = GeneralTable(AllObservation.objects.filter(ref=reference))
    return render(request, 'ref_detail.html', {'references': table, 'reference' : reference})

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
