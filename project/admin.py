from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # ¿Qué columnas quieres ver en la lista principal?
    list_display = ("title", "technology", "created_at")

    # ¿Quieres un buscador por título?
    search_fields = ("title", "technology")

    # ¿Quieres filtros laterales por fecha o tecnología?
    list_filter = ("technology", "created_at")
