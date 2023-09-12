from django.contrib import admin
from .models import *



lp=25


class ModePaiementAdmin(admin.ModelAdmin):
    list_per_page = lp
    list_display = ('mode','supprimer',)
    readonly_fields = ('supprimer',)
    list_filter = ('supprimer',)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

admin.site.register(ModePaiement, ModePaiementAdmin)