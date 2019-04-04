from django.forms import ModelForm
from django import forms
from .models import Details
from django.contrib.auth.models import User

class DeliveryForm(ModelForm):
    class Meta:
        model = Details
        exclude = ('orderdate','delivered')


CHOICES=[('SF','SDF'),
         ('SFSD','SDF')]

class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=[CHOICES], widget=forms.RadioSelect)        