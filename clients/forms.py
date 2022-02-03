from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm, forms
from main.models import *

class RequestForm(ModelForm):
    class Meta:
        model = repairRequest
        fields = ['author', 'contacts', 'brandCar', 'problem']
