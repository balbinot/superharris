from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from catalogue.models import GlobularCluster, Observation, Reference
import django_tables2 as tables
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.template.loader import get_template
from catalogue.forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

class ObservationTable(tables.Table):
    id = 'table'
    class Meta:
        model = Observation

def index(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'index.html', {'observations': Observation.objects.all()})


def references(request):
    return render(request, 'references.html', {'references': Reference.objects.all()})


def detail(request, cluster_id_id):
    cluster = get_object_or_404(GlobularCluster, pk=cluster_id_id)
    return render(request, 'detail.html', {'observations': Observation.objects.filter(cluster_id=cluster), 'cluster' : cluster})


def view1(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'view1.html')


def view2(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'view2.html')


def view3(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'view3.html')

def registered(request):
    return render(request, 'registered.html')

def submit(request):
    return render(request, 'submit.html')

def submitted(request):
    return render(request, 'submitted.html')

@login_required
def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/catalogue/')

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/catalogue/')
            else:
                return HttpResponse("Account disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'login.html', locals())

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(
        username=form.cleaned_data['username'],
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password1']
      )
      return HttpResponseRedirect('../registered/')
  else:
    form = RegistrationForm()

  return render(request, 'register.html', {'form': form})

class SubmitView(FormView):
    template_name = 'submit.html'
    form_class = SubmitForm
    success_url = '../submitted/'

    def form_valid(self, form):
        return super(SubmitView, self).form_valid(form)


def submit(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            model = Submitted()

            cluster_name = request.POST['cluster']
            cluster_id = [g for g in GC.objects.all() if g.cluster_id == cluster_name][0]
            model.cluster_id = cluster_id
            model.name = request.POST['name']
            model.ra = request.POST['ra']
            model.dec = request.POST['dec']
            model.gallon = request.POST['gallon']
            model.gallat = request.POST['gallat']
            model.dfs = request.POST['dfs']
            model.metallicity = request.POST['metallicity']
            model.w_mean_met = request.POST['w_mean_met']
            model.m_v_t = request.POST['m_v_t']
            model.ph_u_b = request.POST['ph_u_b']
            model.ph_b_v = request.POST['ph_b_v']
            model.ph_v_r = request.POST['ph_v_r']
            model.ph_v_i = request.POST['ph_v_i']
            model.ellipticity = request.POST['ellipticity']
            model.v_r = request.POST['v_r']
            model.sig_v = request.POST['sig_v']
            model.sig_err = request.POST['sig_err']
            model.sp_c = request.POST['sp_c']
            model.sp_r_c = request.POST['sp_r_c']
            model.sp_r_h = request.POST['sp_r_h']
            model.sp_mu_V = request.POST['sp_mu_V']
            model.sp_rho_0 = request.POST['sp_rho_0']
            model.comment = request.POST['comment']

            model.save()
            return HttpResponseRedirect('../submitted/')
        else:
            print('LALALA')
            print(form.errors)

    else:
        form = SubmitForm()
    return render(request, 'submit.html', {'form': form})
