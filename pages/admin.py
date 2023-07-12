from django.contrib import admin

from .models import Propiedad, Imagen

# Register your models here.


class ImagenesInline(admin.TabularInline):
    model = Imagen
    extra = 1


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    inlines = [ImagenesInline]
    list_display = (
        "nombre",
        "apellido",
        "direccion",
        "numero_direccion",
        "precio",
    )  # Campos a mostrar en la lista
    list_filter = (
        "metros_cuadrados",
        "precio",
        "ambientes",
        "habitaciones",
    )  # Filtros en la barra lateral
    search_fields = ("nombre", "apellido", "direccion")  # Campos de búsqueda
    fieldsets = (
        (
            "Información de la Propiedad",
            {
                "fields": (
                    "nombre",
                    "apellido",
                    "direccion",
                    "numero_direccion",
                    "precio",
                    "dolares",
                    "categoria",
                    "destacado",
                )
            },
        ),
        (
            "Detalles",
            {
                "fields": (
                    "metros_cuadrados",
                    "ambientes",
                    "habitaciones",
                    "baños",
                    "garage",
                    'info_extra'
                )
            },
        ),
        (
            "Otros",
            {
                "fields": (
                    "duracion_contrato",
                    "expensas",
                    "niños",
                    "mascotas",
                    "antiguedad",
                )
            },
        ),
        ("Información de Contacto", {"fields": ("correo", "telefono")}),
    )


admin.site.register(Imagen)
