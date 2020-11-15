from django.contrib import admin

from kadai2.models import SexModel


class SexModelAdmin(admin.ModelAdmin):
    list_display = ['sex_id', 'value', 'create_dt']


admin.site.register(SexModel, SexModelAdmin)
