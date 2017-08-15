from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Reference)
admin.site.register(GlobularCluster)
admin.site.register(AllObservation)
