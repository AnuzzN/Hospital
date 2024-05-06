from django.contrib import admin

from doctor.models import district, doctors, place 

# Register your models here.

class doctorsAdmin(admin.ModelAdmin):
    list_display=['fname','Specialisation','visitingtime']
    
admin.site.register(doctors,doctorsAdmin) 
admin.site.register(place) 
admin.site.register(district)   