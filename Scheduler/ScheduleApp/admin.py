from django.contrib import admin
from .models import Employee
from .models import Event
from .models import Shift
# Register your models here.
admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(Shift)