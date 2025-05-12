import os

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory, Select, CharField, ModelForm, IntegerField, modelformset_factory
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from .models import Person


GetAllPersonForms = modelformset_factory(Person, fields="__all__")
CreateNewPersonForms = modelformset_factory(Person, fields="__all__", extra=3)




def validate_title(value):
    if value == "Last year snow":
        raise ValidationError("Baned title")



class PersonModelForm(ModelForm):
    age = IntegerField(label="Your age", min_value=18)
    first_name = CharField(required=True, validators=[validate_title])

    class Meta:
        model = Person
        fields = "__all__"


PersonForm = modelform_factory(
    Person,
    fields=("first_name" ,"last_name"),
    # widgets={"first_name": Select(attrs={"size": 8})},
    labels={"last_name": "surname"},
    help_texts={"first_name": "Example Misha"},
    field_classes={"first_name": CharField}
)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)