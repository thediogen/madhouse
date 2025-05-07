import os

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory, Select, CharField, ModelForm, IntegerField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from .models import Person

def make_mistake(value):
    if value > 16:
        raise ValidationError(
            gettext_lazy("MISTAKE"),
            params={"value": value}
        )





class PersonModelForm(ModelForm):
    age = IntegerField(label="Your age", validators=[make_mistake])

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