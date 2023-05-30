from django import forms
from .views import *
from .models import *


class SargytForm(forms.ModelForm):
    class Meta:
        model = Sargyt
        fields = ('lastname',
                  'surname',
                  'address',
                  'phone')

