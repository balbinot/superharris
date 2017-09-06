from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Reference)
admin.site.register(GlobularCluster)
admin.site.register(Observation)

class SubmittedAdmin(admin.ModelAdmin):
    fields = ('created_at', 'cluster_id', 'name', 'ra', 'dec', 'gallon', 'gallat', 'dfs', 'metallicity', 'w_mean_met', 'm_v_t', 'ph_u_b', 'ph_b_v', 'ph_v_r', 'ph_v_i', 'ellipticity', 'v_r, sig_v', 'sig_err', 'sp_c', 'sp_r_c', 'sp_r_h', 'sp_mu_V', 'sp_rho_0', 'comment')
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
