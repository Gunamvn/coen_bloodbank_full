from django.forms import ModelForm
from .models import bbank
from .models import donarreg

class CreateForm(ModelForm):
    class Meta:
        model = bbank
        fields = ['firstname', 'lastname', 'user_age', 'bloodgrp', 'email', 'user_address']

class DonarForm(ModelForm):
    class Meta:
        model = donarreg
        fields = ['firstname', 'lastname', 'user_age', 'bloodgrp', 'email', 'user_address']
