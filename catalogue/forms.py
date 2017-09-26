import re   #Regular expression library
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from catalogue.models import Submitted
from models import GlobularCluster as GC
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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

  def __init__(self, *args, **kwargs):
      super(RegistrationForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.form_id = 'id-registrationForm'
      self.helper.form_class = 'blueForms'
      self.helper.form_method = 'post'
      self.helper.form_action = 'register'
      self.helper.form_class = 'form-horizontal'

      self.fields['username'].widget.attrs['placeholder'] = u'Enter here'
      self.fields['email'].widget.attrs['placeholder'] = u'Enter here'
      self.fields['password1'].widget.attrs['placeholder'] = u'Enter here'
      self.fields['password2'].widget.attrs['placeholder'] = u'Enter here'

      self.helper.layout = Layout(
          Div(
              Div('username', css_class='col-xs-6'),
          css_class='row-fluid'),
          Div(
              Div('email', css_class='col-xs-6'),
          css_class='row-fluid'),
          Div(
              Div('password1', css_class='col-xs-6'),
          css_class='row-fluid'),
          Div(
              Div('password2', css_class='col-xs-6'),
          css_class='row-fluid'),
          )
      self.helper.add_input(Submit('submit', 'Submit'))

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
    comment = forms.CharField(label = "Comments", max_length=50, widget=forms.Textarea, required=False)


    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-submitForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.form_class = 'form-horizontal'

        self.fields['name'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ra'].widget.attrs['placeholder'] = u'Enter here [degrees]'
        self.fields['dec'].widget.attrs['placeholder'] = u'Enter here [degrees]'
        self.fields['gallon'].widget.attrs['placeholder'] = u'Enter here [degrees]'
        self.fields['gallat'].widget.attrs['placeholder'] = u'Enter here [degrees]'
        self.fields['dfs'].widget.attrs['placeholder'] = u'Enter here[kpc]'
        self.fields['metallicity'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['w_mean_met'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['m_v_t'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ph_u_b'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ph_b_v'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ph_v_r'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ph_v_i'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['ellipticity'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['v_r'].widget.attrs['placeholder'] = u'Enter here [km/s]'
        self.fields['sig_v'].widget.attrs['placeholder'] = u'Enter here [km/s]'
        self.fields['sig_err'].widget.attrs['placeholder'] = u'Enter here [km/s]'
        self.fields['sp_c'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['sp_r_c'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['sp_r_h'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['sp_mu_V'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['sp_rho_0'].widget.attrs['placeholder'] = u'Enter here'
        self.fields['comment'].widget.attrs['placeholder'] = u'Enter here'

        #self.helper.label_class = 'col-lg-2'
        #self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Fieldset('Name and reference',
                Div('cluster', css_class='col-xs-6'),
                Div('name', css_class='col-xs-6'),
            css_class='row-fluid'),

            Fieldset('Observational data',
                Div('ra', css_class='col-xs-6'),
                Div('dec', css_class='col-xs-6'),
            css_class='row-fluid'),
            Div(
                Div('gallon', css_class='col-xs-6'),
                Div('gallat', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('dfs', css_class='col-xs-6'),
                Div('metallicity', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('w_mean_met', css_class='col-xs-6'),
                Div('m_v_t', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('ph_u_b', css_class='col-xs-6'),
                Div('ph_b_v', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('ph_v_r', css_class='col-xs-6'),
                Div('ph_v_i', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('ellipticity', css_class='col-xs-6'),
                Div('v_r', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('sig_v', css_class='col-xs-6'),
                Div('sig_err', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('sp_c', css_class='col-xs-6'),
                Div('sp_r_c', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('sp_r_h', css_class='col-xs-6'),
                Div('sp_mu_V', css_class='col-xs-6',),
            css_class='row-fluid'),
            Div(
                Div('sp_rho_0', css_class='col-xs-6'),
            css_class='row-fluid'),
            Fieldset('Additional information',
                Div('comment', css_class='col-xs-6'),
            css_class='row-fluid'),
            )
        self.helper.add_input(Submit('submit', 'Submit'))
