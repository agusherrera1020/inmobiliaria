import uuid

from django.db import models
from django.urls import reverse

# Create your models here.


class Propiedad(models.Model):
    precio = models.IntegerField(verbose_name="Precio")
    dolares = models.BooleanField(verbose_name="Dolares")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    numero_direccion = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Número de Dirección",
    )
    categoria = models.CharField(
        max_length=10,
        choices=[("Alquiler", "Alquiler"), ("Venta", "Venta")],
        verbose_name="Categoría",
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    correo = models.CharField(max_length=100, verbose_name="Dirección Electrónica")
    telefono = models.CharField(max_length=50, verbose_name="Número Telefónico")
    metros_cuadrados = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Metros Cuadrados",
    )
    habitaciones = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Habitaciones",
    )
    ambientes = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Ambientes",
    )
    baños = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Baños",
    )
    niños = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        choices=[("Si", "Si"), ("No", "No")],
        verbose_name="Niños",
    )
    mascotas = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        choices=[("Si", "Si"), ("No", "No")],
        verbose_name="Mascotas",
    )
    garage = models.IntegerField(
        blank=True, null=True, verbose_name="Espacio del Garage"
    )
    duracion_contrato = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Duración del Contrato"
    )
    expensas = models.IntegerField(blank=True, null=True, verbose_name="Expensas")
    antiguedad = models.IntegerField(
        blank=True, null=True, verbose_name="Antigüedad de la Construcción"
    )
    info_extra = models.TextField(blank=True, null=True, verbose_name="Información extra")
    destacado = models.BooleanField(verbose_name="Destacado")

    class Meta:
        verbose_name_plural = "Propiedades"

    def get_absolute_url(self):
        return reverse("detalles", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Imagen(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes/")

    class Meta:
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return f"{self.propiedad.direccion} ({self.propiedad.nombre} {self.propiedad.apellido})"
