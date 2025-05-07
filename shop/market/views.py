import time
import traceback

from django.http import HttpResponse, HttpResponseBadRequest, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Min, Max
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.contrib import messages

from django.core.paginator import Paginator

from .models import Person, Stuff
from .forms import PersonForm, PersonModelForm


def index(request):

    context = {
        "title": "main"
    }

    return render(request, 'index.html', context)



def get_person_by_pk(request, pk: int):
    try:
        person = Person.objects.get(pk=pk)
        return HttpResponse(f"{person}")
    except ObjectDoesNotExist:
        return HttpResponse(f"error: Person with {pk} does not exists")

def get_person_by_surname(request, surname: str):
    person = Person.objects.get(last_name=surname)
    return HttpResponse(f"{person}")


def get_or_create_person(request, pk:int):
    person = Person.objects.get_or_create(
        pk=pk,
        defaults={
            "first_name": "John",
            "last_name": "Sina"
        }
    )

    return HttpResponse(f"{person}")


def change_surname(request, pk: int, surname: str):
    try:
        person = Person.objects.get(pk=pk)

        person.last_name = surname
        person.save()

        return HttpResponse(f"New surname for user - {person.first_name}, {person.last_name}")

    except ObjectDoesNotExist:
        return HttpResponseBadRequest(
            {
                "error": f"Person with {pk} does not exists",
                "traceback": traceback.format_exc()
            }
        )


def create_person(request):
    p = Person(first_name="Patrick", last_name="Saint")

    p.save()
    return HttpResponse("Created")


def update_or_create_person(request, name:str):
    person = Person.objects.update_or_create(
        first_name=name,
        defaults={
            "first_name": "Oguzik",
            "last_name": "Lavrov"
        }
    )
    return HttpResponse(f"{person}")


def delete_person(request, pk: int):
    person = Person.objects.get(
        pk=pk,
    )
    person.delete()
    return HttpResponse(f"Deleted person")

def get_all_persons(request):
    persons = Person.objects.aggregate(Min("first_name"))
    print(persons["first_name__min"])
    for person in persons:
        print(person)

    return render(request, "persons.html", context={"persons": persons})


def request_info_check(request):
    info = []

    # Основні атрибути
    info.append(f"Method: {request.method}")
    info.append(f"Scheme: {request.scheme}")
    info.append(f"Path: {request.path}")
    info.append(f"Encoding: {request.encoding}")
    info.append(f"Content-Type: {request.content_type}")
    info.append(f"Content Params: {request.content_params}")
    # GET і POST параметри
    info.append(f"GET params: {dict(request.GET)}")
    info.append(f"POST params: {dict(request.POST)}")

    # Файли
    info.append(f"FILES: {[f.name for f in request.FILES.values()]}")

    # META-поля (тільки кілька, бо їх дуже багато)
    meta_keys = [
        'CONTENT_LENGTH', 'CONTENT_TYPE', 'HTTP_USER_AGENT',
        'HTTP_ACCEPT', 'HTTP_HOST', 'HTTP_REFERER',
        'REMOTE_ADDR', 'REMOTE_HOST', 'REMOTE_USER',
        'QUERY_STRING', 'SERVER_NAME', 'REQUEST_METHOD'
    ]
    for key in meta_keys:
        info.append(f"META[{key}]: {request.META.get(key)}")

    # resolver_match
    info.append(f"Resolver match: {request.resolver_match}")

    # Заголовки (Django 2.2+)
    if hasattr(request, 'headers'):
        headers = '\n'.join([f"{k}: {v}" for k, v in request.headers.items()])
        info.append("Headers:\n" + headers)

    # Додаткові методи
    info.append(f"Host: {request.get_host()}")
    info.append(f"Port: {request.get_port()}")
    info.append(f"Full Path: {request.get_full_path()}")
    info.append(f"Absolute URL: {request.build_absolute_uri()}")
    info.append(f"Is secure: {request.is_secure()}")

    # AJAX-перевірка
    if hasattr(request, 'is_ajax'):  # Застаріле, але покажемо
        info.append(f"Is AJAX: {request.is_ajax()}")

    return HttpResponse("<br>".join(info), content_type="text/html")


def index22(request):
    resp = HttpResponse("Here will be\n", content_type='text/plain; charset=utf-8')
    resp.write('Головна - ')
    resp.writelines(('page\n', 'site\n'))
    resp['keywords'] = 'Python, Django'
    return resp


def stream_view(request):
    def event_stream():
        for i in range(5):
            yield f"data: {i}\n\n"
            time.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


@require_http_methods(["GET", "POST"])
def tutorial(request):
    return HttpResponseRedirect(reverse('get_person_by_pk', kwargs={"pk": 1}))


class AboutAs(TemplateView):
    template_name = "about.html"



def get_all_stuff(request):
    context = {
        'all_stuff': Stuff.objects.all(),
    }

    return render(request, "products.html", context)


def get_all_product_2(request):
    all_products = Stuff.objects.all()
    paginator = Paginator(all_products, 1)

    if "page" in request.GET:
        page_num = request.GET.get('page', 1)
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    return render(request, "products.html", {"page": page, "products": page.object_list})


def create_person_form(request):
    if request.method == "POST":
        new_form = PersonModelForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect("index")

        else:
            messages.warning(request, "Wrond data")

    new_form = PersonModelForm()
    context = {"form": new_form}
    return render(request, "forms.html", context)

# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful")
#             return redirect("index")
#         else:
#             return render(request, '400.html')
#
#     form = NewUserForm()
#     return render(request=request, template_name="register.html", context={"register_form": form})
