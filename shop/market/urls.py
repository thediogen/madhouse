from django.urls import path
from django.views.generic import TemplateView

from .views import (index, get_person_by_pk, get_person_by_surname, change_surname, get_or_create_person,
                    update_or_create_person, create_person, delete_person, get_all_persons, request_info_check,
                    index22, tutorial, AboutAs, get_all_stuff, get_all_product_2, create_person_form)

urlpatterns = [
    path("", index, name="index"),
    path("get/<int:pk>", get_person_by_pk, name="get_person_by_pk"),
    path("get/<str:surname>", get_person_by_surname),
    path("get_or_create_person/<int:pk>", get_or_create_person),
    path("change_surname/<int:pk>/<str:surname>", change_surname),
    path("update/<str:name>", update_or_create_person),
    path("create", create_person),
    path("delete/<int:pk>", delete_person),
    path("all", get_all_persons),
    path("check", request_info_check),
    path("v2", index22, name="index22"),
    path("reverse", tutorial),
    path("about", AboutAs.as_view(), name="about"),
    path("about2/", TemplateView.as_view(template_name="about.html")),
    path("products2", get_all_product_2),
    path("forms", create_person_form)
]
