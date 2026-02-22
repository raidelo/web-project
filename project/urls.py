from django.urls import path

from .views import project_detail, project_list

urlpatterns = [
    path("", project_list, name="project_list"),
    path("project<int:pk>", project_detail, name="project_detail"),
]
