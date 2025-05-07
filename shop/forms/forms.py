from django.forms import ModelForm, CharField, TextInput, Textarea

from .models import Articles

class ArticleForms(ModelForm):
    class Meta:
        model = Articles
        exclude = []
