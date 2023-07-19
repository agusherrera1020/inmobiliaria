from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

from .forms import PropiedadForm, ImagenForm
from .models import Propiedad, Imagen

# Create your views here.


class PropiedadListView(generic.ListView):
    model = Propiedad
    template_name = "pages/propiedades.html"
    context_object_name = "propiedades"
    ordering = ["-destacado"]

    def get_queryset(self):
        queryset = super().get_queryset()

        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        
        return queryset


class PropiedadDetailView(generic.DetailView):
    model = Propiedad
    template_name = "pages/detalles.html"


class ContactoView(generic.TemplateView):
    template_name = "pages/contacto.html"
