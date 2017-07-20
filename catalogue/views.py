from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from catalogue.models import GlobularCluster, Observation, Reference
import django_tables2 as tables
from django.shortcuts import get_object_or_404, render

class ObservationTable(tables.Table):
    class Meta:
        model = Observation

def index(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'index.html', {'observations': Observation.objects.all(), 'references': Reference.objects.all()})


def references(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'references.html', {'references': Reference.objects.all()})


def detail(request, cluster_id_id):
    cluster = get_object_or_404(GlobularCluster, pk=cluster_id_id)
    return render(request, 'detail.html', {'observations': Observation.objects.filter(cluster_id=cluster)})




