from django.contrib import admin

from patient.models import district, patients, state

# Register your models here.


class patientsAdmin(admin.ModelAdmin):
    list_display=['fname','disease','visitingdoctor']
    


admin.site.register(patients,patientsAdmin)  
admin.site.register(state)
admin.site.register(district)
