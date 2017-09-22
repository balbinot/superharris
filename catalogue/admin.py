from django.contrib import admin
from .models import *

admin.site.register(Reference)
admin.site.register(GlobularCluster)
admin.site.register(Observation)

def Reject(modeladmin, request, queryset):
    for cluster in queryset:
        if cluster.status == REJECTED:
            cluster.status == REJECTED
            cluster.save()
Reject.short_description = 'Rejected'

def Accept(modeladmin, request, queryset):
    for cluster in queryset:
        if cluster.status == ACCEPTED:
            cluster.status == ACCEPTED
            cluster.save()
Accept.short_description = 'Accepted'

'''def Sub_Accept(modeladmin, request, queryset):
    for cluster in queryset:
        if cluster.status == ACCEPTED:
            cluster.save()
Accept.short_description = 'Accepted' '''

class SubmittedAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'created_by', 'status']
    actions  = [Reject, Accept]
admin.site.register(Submitted, SubmittedAdmin)
