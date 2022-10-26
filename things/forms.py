"""Forms of the project."""

from django import forms
from .models import Thing

class SignUpForm(forms.ModelForm):
    #allows us to relate form to models
    class Meta:
        model = Thing;
        fields = ('name', 'description' , 'quantity')
        widgets = {'description' :forms.Textarea(),'quantity':forms.NumberInput()}


#now if we change validation constraints within user models - form changes as well
