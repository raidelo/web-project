from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Project


def project_list(request: HttpRequest) -> HttpResponse:
    # Traemos todos los objetos de la tabla Project
    projects = Project.objects.all()  # pyright: ignore[reportAttributeAccessIssue]

    # Creamos el 'contexto': un diccionario con los datos para el HTML
    context = {"projects": projects}

    # Renderizamos la página pasando los datos
    return render(request, "projects/project_list.html", context)


def project_detail(request: HttpRequest, pk: int) -> HttpResponse:
    project = Project.objects.get(pk=pk)  # pyright: ignore[reportAttributeAccessIssue]
    return render(request, "projects/project_detail.html", {"project": project})
