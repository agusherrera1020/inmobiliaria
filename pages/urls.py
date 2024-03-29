from django.urls import path

from . import views

urlpatterns = [
    path("", views.PropiedadListView.as_view(), name="propiedades"),
    path("<int:pk>", views.PropiedadDetailView.as_view(), name="detalles"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
]
