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

class UserObs(tables.Table):
    id = 'user_table'
    class Meta:
        model = Submitted

def index(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'index.html', {'observations': Observation.objects.all()})

def user_account(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    user = request.user
    subs = Submitted.objects.filter(created_by=user)
    return render(request, 'account.html', {'user_observations': subs})

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

def store_str(field, placeholder):
    if field != '':
        placeholder = field

def store_float(field, placeholder):
    if field != '':
        placeholder = float(field)

def store_int(field, placeholder):
    if field != '':
        placeholder = int(field)

def submit(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            model = Submitted()
            p = request.POST

            cluster_name = request.POST['cluster']
            cluster_id = [g for g in GC.objects.all() if g.cluster_id == cluster_name][0]
            model.created_by = request.user
            model.cluster_id = cluster_id
            if p['name'] != '':
                model.name = float(p['name'])
            if p['ra'] != '':
                model.ra = float(p['ra'])
            if p['dec'] != '':
                model.dec = float(p['dec'])
            if p['gallon'] != '':
                model.gallon = float(p['gallon'])
            if p['gallat'] != '':
                model.gallat = float(p['gallat'])
            if p['dfs'] != '':
                model.dfs = float(p['dfs'])
            if p['metallicity'] != '':
                model.metallicity = float(p['metallicity'])
            if p['w_mean_met'] != '':
                model.w_mean_met = float(p['w_mean_met'])
            if p['m_v_t'] != '':
                model.m_v_t = float(p['m_v_t'])
            if p['ph_u_b'] != '':
                model.ph_u_b = float(p['ph_u_b'])
            if p['ph_b_v'] != '':
                model.ph_b_v = float(p['ph_b_v'])
            if p['ph_v_r'] != '':
                model.ph_v_r = float(p['ph_v_r'])
            if p['ph_v_i'] != '':
                model.ph_v_i = float(p['ph_v_i'])
            if p['ellipticity'] != '':
                model.ellipticity = float(p['ellipticity'])
            if p['v_r'] != '':
                model.v_r = float(p['v_r'])
            if p['sig_v'] != '':
                model.sig_v = float(p['sig_v'])
            if p['sig_err'] != '':
                model.sig_err = float(p['sig_err'])
            if p['sp_c'] != '':
                model.sp_c = float(p['sp_c'])
            if p['sp_r_c'] != '':
                model.sp_r_c = float(p['sp_r_c'])
            if p['sp_r_h'] != '':
                model.sp_r_h = float(p['sp_r_h'])
            if p['sp_mu_V'] != '':
                model.sp_mu_V = float(p['sp_mu_V'])
            if p['sp_rho_0'] != '':
                model.sp_rho_0 = float(p['sp_rho_0'])
            model.comment = request.POST['comment']

            print('Model : {}'.format(model))
            print(model.ra)
            print(model.dec)
            model.save()
            return HttpResponseRedirect('../submitted/')
        else:
            print(form.errors)

    else:
        form = SubmitForm()
    return render(request, 'submit.html', {'form': form})
