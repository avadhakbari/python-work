from django.contrib import admin

from .models import LaborRegistration,Party,Task,TaskPayment,LaborProfile


# Register your models here.

class laborRegistrationAdmin(admin.ModelAdmin):
    list_display =['labor_id', 'email', 'mobile', 'is_email_verified', 'is_activate']
    search_fields = ['labor_id', 'email', 'mobile']
    list_filter = ['is_email_verified', 'is_activate']
    list_per_page = 10
    list_editable = ['mobile', 'is_email_verified', 'is_activate']


class PartyAdmin(admin.ModelAdmin):
    list_display =['party_id','party_name','party_email','party_mobile','party_address']
    search_fields = ['party_id','party_email','party_mobile']
    list_per_page = 10
    list_editable = ['party_mobile']

admin.site.register(LaborRegistration,laborRegistrationAdmin)
admin.site.register(Party,PartyAdmin)
admin.site.register(Task)
admin.site.register(TaskPayment)
admin.site.register(LaborProfile)
