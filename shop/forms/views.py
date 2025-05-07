from django.shortcuts import render, HttpResponse
from django.template.defaultfilters import title
from django.http import HttpRequest

from .forms import ArticleForms
from .models import Articles


# Create your views here.


def create_get_form(request: HttpRequest):
    if request.method == "POST":
        form = ArticleForms(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Tnx for a new article")
    else:
        context = {}
        form = ArticleForms()
        context["form"] = form

        return render(request, "form.html", context=context)

