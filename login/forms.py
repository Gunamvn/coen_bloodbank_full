from django.forms import ModelForm
from .models import bbank

class CreateForm(ModelForm):
    class Meta:
        model = bbank
        fields = ['firstname', 'lastname', 'user_age', 'bloodgrp', 'email', 'user_address']