#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

UNIT_LENGTH = 32

class GlobularCluster(models.Model):
    cluster_id = models.CharField(max_length=64)

    def __str__(self):
        return self.cluster_id

class Reference(models.Model):
    name     = models.CharField(max_length=256, null=True)
    doi      = models.CharField(max_length=256, null=True, blank=True)
    ads      = models.CharField(max_length=256, null=True, blank=True)
    pub_date = models.DateField('publication date', null=True)

    def __str__(self):
        s = ''
        if self.name:
            s += self.name
        return s

class AllObservation(models.Model):
    ref        = models.ForeignKey(Reference, on_delete=models.CASCADE)
    cluster_id = models.ForeignKey(GlobularCluster, on_delete=models.CASCADE)

    # General fields
    name = models.CharField('Alternate Name', max_length=64, null=True,
                            blank=True)

    # Coordinates
    ra     = models.FloatField('RA', null=True,
                                  blank=True)
    dec    = models.FloatField('DEC', null=True,
                                    blank=True)
    gallon = models.FloatField('Long', null=True, blank=True)
    gallat = models.FloatField('Lat', null=True, blank=True)
    dfs       = models.FloatField('D-sun', null=True,
                                  blank=True)
    dfgc      = models.FloatField('D-GC', null=True,
                                  blank=True)
    gc_x      = models.FloatField('X', null=True,
                                  blank=True)
    gc_y      = models.FloatField('Y', null=True,
                                  blank=True)
    gc_z      = models.FloatField('Z', null=True,
                                  blank=True)
    
    
    

    # Metallicity and Photometry
    metallicity = models.FloatField('Metallicity', null=True, blank=True)
    w_mean_met  = models.FloatField('Weight', null=True,
                                    blank=True)
    FG_red      = models.FloatField('E(B-V)', null=True,
                                    blank=True)
    V_horiz     = models.FloatField('V_HB', null=True,
                                    blank=True)

    app_dist    = models.FloatField('(m-M)V', null=True,
                                    blank=True)
    Int_V_mag   = models.FloatField('V_t', null=True,
                                    blank=True)

    m_v_t       = models.FloatField('Luminosity', null=True, blank=True)
    ph_u_b      = models.FloatField('U-B', null=True, blank=True)
    ph_b_v      = models.FloatField('B-V', null=True, blank=True)
    ph_v_r      = models.FloatField('V-R', null=True, blank=True)
    ph_v_i      = models.FloatField('V-I', null=True, blank=True)
    spec_type   = models.CharField('spt', max_length=64, null=True,
                            blank=True)
    ellipticity = models.FloatField('Ellip',
                                    null=True, blank=True)
    

    # Velocities
    v_r        = models.FloatField('Heliocentric radial velocity', null=True,
                                   blank=True)
    v_err      = models.FloatField('uncertainty', null=True,
                                   blank=True)
    sig_v      = models.FloatField('Velocity dispersion', null=True, blank=True)
    sig_err    = models.FloatField('uncertainty', null=True,
                                   blank=True)
    v_LSR      = models.FloatField('v_LSR', null=True,
                                   blank=True)

    # Structural parameters
    sp_c          = models.FloatField('King-model central concentration',
                                      null=True, blank=True)
    sp_r_c        = models.FloatField('Core radius', null=True, blank=True)
    sp_r_h        = models.FloatField('Half-light radius', null=True,
                                      blank=True)
    sp_mu_V       = models.FloatField('Central surface brightness', null=True,
                                      blank=True)
    sp_rho_0      = models.FloatField('Central luminosity density', null=True,
                                      blank=True)
    lg_tx        = models.FloatField('Core relaxation time', null=True,
                                      blank=True)     
    lg_th        = models.FloatField('Median relaxation time', null=True,
                                      blank=True)

    def __str__(self):
        s = '{} - Ref : {}'.format(str(self.cluster_id), str(self.ref))
        return s


