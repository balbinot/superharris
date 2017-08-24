import re   #Regular expression library
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from catalogue.models import Submitted
from models import GlobularCluster as GC
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import PrependedText, InlineField
#from crispy_forms.bootstrap import InlineField



#class login_page(forms.Form):
 # username = forms.CharField(label='Username', max_length=30)
  #password = forms.CharField(widget=forms.PasswordInput)
  #model = User
  #widgets = {
#      'password': forms.PasswordInput(),
#}

class RegistrationForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  email = forms.EmailField(label='Email', max_length=50)
  password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput()
  )
  password2 = forms.CharField(
    label='Password (Again)',
    widget=forms.PasswordInput()
  )

def clean_password(self):
  if 'password1' in self.cleaned_data:
      password1 = self.Cleaned_data['password1']
      password2 = self.Cleaned_data['password2']
  if password1 == password2:
    return password2
  raise forms.ValidationError('Passwords do not match.')

def clean_username(self):
  username = self.cleaned_data['username']
  if not re.search(r'^\w+$', username):
    raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
  try:
      User.objects.get(username=username)
  except ObjectDoesNotExist:
    return username
  raise forms.ValidationError('Username is already taken :( .')

class SubmitForm(forms.Form):
    gcs = GC.objects.all()
    drop_down_list = [(g, g.cluster_id) for g in gcs]
    drop_down_list.sort(key=lambda x:x[1])

    cluster = forms.ChoiceField(label = "Cluster ID", choices = drop_down_list, required = True)
    name = forms.CharField(label = "Alternative names", max_length = 50, required = False)
    ra = forms.CharField(label = "Right ascension", max_length = 50, required = False)
    dec = forms.CharField(label = "Declination", max_length=50, required=False)
    gallon = forms.CharField(label = "Longitude", max_length=50, required=False)
    gallat = forms.CharField(label = "Latitude", max_length=50, required=False)
    dfs = forms.CharField(label = "Distance from the sun", max_length=50, required=False)
    metallicity = forms.CharField(label = "Metallicity", max_length=50, required=False)
    w_mean_met = forms.CharField(label = "Weight of mean metallicity", max_length=50, required=False)
    m_v_t = forms.CharField(label = "Cluster luminosity", max_length=50, required=False)
    ph_u_b = forms.CharField(label = "U-B", max_length=50, required=False)
    ph_b_v = forms.CharField(label = "B-V", max_length=50, required=False)
    ph_v_r = forms.CharField(label = "V-R", max_length=50, required=False)
    ph_v_i = forms.CharField(label = "V-I", max_length=50, required=False)
    ellipticity = forms.CharField(label = "Projected ellipticity of isophotes", max_length=50, required=False)
    v_r = forms.CharField(label = "Heliocentric radial velocity", max_length=50, required=False)
    sig_v = forms.CharField(label = "Velocity dispersion", max_length=50, required=False)
    sig_err = forms.CharField(label = "Observational uncertainty", max_length=50, required=False)
    sp_c = forms.CharField(label = "King-model central concentration", max_length=50, required=False)
    sp_r_c = forms.CharField(label = "Core radius", max_length=50, required=False)
    sp_r_h = forms.CharField(label = "Half-light radius", max_length=50, required=False)
    sp_mu_V = forms.CharField(label = "Central surface brightness", max_length=50, required=False)
    sp_rho_0 = forms.CharField(label = "Central luminosity density", max_length=50, required=False)
    comment = forms.CharField(label = "Additional comments", max_length=50, widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            PrependedText('cluster', '', placeholder="Select"),
            PrependedText('name', '', placeholder="Enter here")
        )
        self.helper.add_input(Submit('submit', 'Submit'))

'''
class SubmitForm(forms.Form):
    gcs = GC.objects.all()
    drop_down_list = [(g.id, g.cluster_id) for g in gcs]
    drop_down_list.sort(key=lambda x:x[1])

    cluster_id = forms.ChoiceField(choices=drop_down_list, required=Trcluster_id = forms.ChoiceField(choices=drop_down_list, required=True)
    name = forms.CharField(max_length=50, required=False)
    ra = forms.CharField(max_length=50, required=False)
    dec = forms.CharField(max_length=50, required=False)
    gallon = forms.CharField(max_length=50, required=False)
    gallat = forms.CharField(max_length=50, required=False)
    dfs = forms.CharField(max_length=50, required=False)
    metallicity = forms.CharField(max_length=50, required=False)
    w_mean_met = forms.CharField(max_length=50, required=False)
    m_v_t = forms.CharField(max_length=50, required=False)
    ph_u_b = forms.CharField(max_length=50, required=False)
    ph_b_v = forms.CharField(max_length=50, required=False)
    ph_v_r = forms.CharField(max_length=50, required=False)
    ph_v_i = forms.CharField(max_length=50, required=False)
    ellipticity = forms.CharField(max_length=50, required=False)
    v_r = forms.CharField(max_length=50, required=False)
    sig_v = forms.CharField(max_length=50, required=False)
    sig_err = forms.CharField(max_length=50, required=False)
    sp_c = forms.CharField(max_length=50, required=False)
    sp_r_c = forms.CharField(max_length=50, required=False)
    sp_r_h = forms.CharField(max_length=50, required=False)
    sp_mu_V = forms.CharField(max_length=50, required=False)
    sp_rho_0 = forms.CharField(max_length=50, required=False)
    comment = forms.CharField(max_length=50, widget=forms.Textarea,  required=False) '''
