from django.urls import path

from . import views

urlpatterns = [
    path("", views.InicioPageView.as_view(), name="inicio"),
    path("propiedades/", views.PropiedadListView.as_view(), name="propiedades"),
    path("propiedades/<int:pk>", views.PropiedadDetailView.as_view(), name="detalles"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
]
