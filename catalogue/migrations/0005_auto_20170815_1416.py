# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20170815_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.FloatField(blank=True, null=True, verbose_name='RA')),
                ('dec', models.FloatField(blank=True, null=True, verbose_name='DEC')),
                ('gallon', models.FloatField(blank=True, null=True, verbose_name='Long')),
                ('gallat', models.FloatField(blank=True, null=True, verbose_name='Lat')),
                ('dfs', models.FloatField(blank=True, null=True, verbose_name='D-sun')),
                ('dfgc', models.FloatField(blank=True, null=True, verbose_name='D-GC')),
                ('gc_x', models.FloatField(blank=True, null=True, verbose_name='X')),
                ('gc_y', models.FloatField(blank=True, null=True, verbose_name='Y')),
                ('gc_z', models.FloatField(blank=True, null=True, verbose_name='Z')),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.GlobularCluster')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Reference')),
            ],
        ),
        migrations.CreateModel(
            name='MetallicityAndPhotometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metallicity', models.FloatField(blank=True, null=True, verbose_name='Metallicity')),
                ('w_mean_met', models.FloatField(blank=True, null=True, verbose_name='Weight')),
                ('FG_red', models.FloatField(blank=True, null=True, verbose_name='E(B-V)')),
                ('V_horiz', models.FloatField(blank=True, null=True, verbose_name='V_HB')),
                ('app_dist', models.FloatField(blank=True, null=True, verbose_name='(m-M)V')),
                ('Int_V_mag', models.FloatField(blank=True, null=True, verbose_name='V_t')),
                ('m_v_t', models.FloatField(blank=True, null=True, verbose_name='Luminosity')),
                ('ph_u_b', models.FloatField(blank=True, null=True, verbose_name='U-B')),
                ('ph_b_v', models.FloatField(blank=True, null=True, verbose_name='B-V')),
                ('ph_v_r', models.FloatField(blank=True, null=True, verbose_name='V-R')),
                ('ph_v_i', models.FloatField(blank=True, null=True, verbose_name='V-I')),
                ('spec_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='spt')),
                ('ellipticity', models.FloatField(blank=True, null=True, verbose_name='Ellip')),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.GlobularCluster')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Reference')),
            ],
        ),
        migrations.CreateModel(
            name='VelocitiesAndStructuralParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_r', models.FloatField(blank=True, null=True, verbose_name='Heliocentric radial velocity')),
                ('v_err', models.FloatField(blank=True, null=True, verbose_name='uncertainty')),
                ('sig_v', models.FloatField(blank=True, null=True, verbose_name='Velocity dispersion')),
                ('sig_err', models.FloatField(blank=True, null=True, verbose_name='uncertainty')),
                ('v_LSR', models.FloatField(blank=True, null=True, verbose_name='v_LSR')),
                ('sp_c', models.FloatField(blank=True, null=True, verbose_name='King-model central concentration')),
                ('sp_r_c', models.FloatField(blank=True, null=True, verbose_name='Core radius')),
                ('sp_r_h', models.FloatField(blank=True, null=True, verbose_name='Half-light radius')),
                ('sp_mu_V', models.FloatField(blank=True, null=True, verbose_name='Central surface brightness')),
                ('sp_rho_0', models.FloatField(blank=True, null=True, verbose_name='Central luminosity density')),
                ('lg_tx', models.FloatField(blank=True, null=True, verbose_name='Core relaxation time')),
                ('lg_th', models.FloatField(blank=True, null=True, verbose_name='Median relaxation time')),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.GlobularCluster')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Reference')),
            ],
        ),
        migrations.RenameModel(
            old_name='Observation',
            new_name='AllObservation',
        ),
    ]
