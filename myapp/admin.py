from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(patient)
admin.site.register(Doctor)
admin.site.register(Ward)
admin.site.register(Appointment)
admin.site.register(Contact)






