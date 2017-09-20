# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20170301_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Alternative names')),
                ('ra', models.FloatField(blank=True, null=True, verbose_name='Right ascension [degree]')),
                ('dec', models.FloatField(blank=True, null=True, verbose_name='Declinations [degree]')),
                ('gallon', models.FloatField(blank=True, null=True, verbose_name='Longitude [degree]')),
                ('gallat', models.FloatField(blank=True, null=True, verbose_name='Latitude [degree]')),
                ('dfs', models.FloatField(blank=True, null=True, verbose_name='Distance from the sun [kpc]')),
                ('metallicity', models.FloatField(blank=True, null=True, verbose_name='Metallicity')),
                ('w_mean_met', models.FloatField(blank=True, null=True, verbose_name='Weight of mean metallicity')),
                ('m_v_t', models.FloatField(blank=True, null=True, verbose_name='Cluster luminosity')),
                ('ph_u_b', models.FloatField(blank=True, null=True, verbose_name='U-B')),
                ('ph_b_v', models.FloatField(blank=True, null=True, verbose_name='B-V')),
                ('ph_v_r', models.FloatField(blank=True, null=True, verbose_name='V-R')),
                ('ph_v_i', models.FloatField(blank=True, null=True, verbose_name='V-I')),
                ('ellipticity', models.FloatField(blank=True, null=True, verbose_name='Projected ellipticity of isophotes')),
                ('v_r', models.FloatField(blank=True, null=True, verbose_name='Heliocentric radial velocity [km/s]')),
                ('sig_v', models.FloatField(blank=True, null=True, verbose_name='Velocity dispersion [km/s]')),
                ('sig_err', models.FloatField(blank=True, null=True, verbose_name='Observational uncertainty [km/s]')),
                ('sp_c', models.FloatField(blank=True, null=True, verbose_name='King-model central concentration')),
                ('sp_r_c', models.FloatField(blank=True, null=True, verbose_name='Core radius')),
                ('sp_r_h', models.FloatField(blank=True, null=True, verbose_name='Half-light radius')),
                ('sp_mu_V', models.FloatField(blank=True, null=True, verbose_name='Central surface brightness')),
                ('sp_rho_0', models.FloatField(blank=True, null=True, verbose_name='Central luminosity density')),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='Additional comments')),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.GlobularCluster')),
            ],
        ),
    ]
