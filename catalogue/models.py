#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


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
        if self.doi:
            s += '(doi:{})'.format(self.doi)
        return s

class Observation(models.Model):
    ref        = models.ForeignKey(Reference, on_delete=models.CASCADE)
    cluster_id = models.ForeignKey(GlobularCluster, on_delete=models.CASCADE)

    # General fields
    name = models.CharField('Alternative names', max_length=64, null=True,
                            blank=True)

    # Coordinates
    ra     = models.FloatField('Right ascension [degree]', null=True,
                                  blank=True)
    dec    = models.FloatField('Declinations [degree]', null=True,
                                    blank=True)
    gallon = models.FloatField('Longitude [degree]', null=True, blank=True)
    gallat = models.FloatField('Latitude [degree]', null=True, blank=True)
    dfs       = models.FloatField('Distance from the sun [kpc]', null=True,
                                  blank=True)

    # Metallicity
    metallicity = models.FloatField('Metallicity', null=True, blank=True)
    w_mean_met  = models.FloatField('Weight of mean metallicity', null=True,
                                    blank=True)

    m_v_t       = models.FloatField('Cluster luminosity', null=True, blank=True)
    ph_u_b      = models.FloatField('U-B', null=True, blank=True)
    ph_b_v      = models.FloatField('B-V', null=True, blank=True)
    ph_v_r      = models.FloatField('V-R', null=True, blank=True)
    ph_v_i      = models.FloatField('V-I', null=True, blank=True)
    ellipticity = models.FloatField('Projected ellipticity of isophotes',
                                    null=True, blank=True)

    # Velocities
    v_r        = models.FloatField('Heliocentric radial velocity [km/s]', null=True,
                                   blank=True)
    sig_v      = models.FloatField('Velocity dispersion [km/s]', null=True, blank=True)
    sig_err    = models.FloatField('Observational uncertainty [km/s]', null=True,
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

    def __str__(self):
        s = '{} - Ref : {}'.format(str(self.cluster_id), str(self.ref))
        return s

class Submitted(models.Model):
    VALIDATE = 1
    ACCEPTED = 2
    REJECTED = 3

    STATUS_CHOICES = (
        (VALIDATE, 'To be validated'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )

    created_by = models.ForeignKey(User, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cluster_id = models.ForeignKey(GlobularCluster, on_delete=models.CASCADE)
    name = models.CharField('Alternative names', max_length=64, null=True, blank=True)
    ra = models.FloatField('Right ascension [degree]', null=True, blank=True)
    dec = models.FloatField('Declinations [degree]', null=True, blank=True)
    gallon = models.FloatField('Longitude [degree]', null=True, blank=True)
    gallat = models.FloatField('Latitude [degree]', null=True, blank=True)
    dfs       = models.FloatField('Distance from the sun [kpc]', null=True, blank=True)
    metallicity = models.FloatField('Metallicity', null=True, blank=True)
    w_mean_met  = models.FloatField('Weight of mean metallicity', null=True, blank=True)
    m_v_t = models.FloatField('Cluster luminosity', null=True, blank=True)
    ph_u_b = models.FloatField('U-B', null=True, blank=True)
    ph_b_v = models.FloatField('B-V', null=True, blank=True)
    ph_v_r = models.FloatField('V-R', null=True, blank=True)
    ph_v_i = models.FloatField('V-I', null=True, blank=True)
    ellipticity = models.FloatField('Projected ellipticity of isophotes', null=True, blank=True)
    v_r = models.FloatField('Heliocentric radial velocity [km/s]', null=True, blank=True)
    sig_v = models.FloatField('Velocity dispersion [km/s]', null=True, blank=True)
    sig_err = models.FloatField('Observational uncertainty [km/s]', null=True, blank=True)
    sp_c = models.FloatField('King-model central concentration', null=True, blank=True)
    sp_r_c = models.FloatField('Core radius', null=True, blank=True)
    sp_r_h = models.FloatField('Half-light radius', null=True, blank=True)
    sp_mu_V = models.FloatField('Central surface brightness', null=True, blank=True)
    sp_rho_0 = models.FloatField('Central luminosity density', null=True, blank=True)
    comment = models.CharField('Additional comments', max_length=64, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=VALIDATE)

    def __str__(self):
        data = '{} - Ref : {}'.format(str(self.cluster_id), str(self.cluster_id))
        return data
