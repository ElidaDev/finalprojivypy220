from django import forms
from .models import *

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'
        #if you want to use all fields just do fields = '__all__'
class ShiftEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'