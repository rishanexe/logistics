from django.forms import ModelForm
from .models import Details
from django.contrib.auth.models import User

class DeliveryForm(ModelForm):
    class Meta:
        model = Details
        exclude = ('orderdate',)