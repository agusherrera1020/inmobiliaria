from django import forms
from django.core.mail import send_mail
from .models import Propiedad, Imagen

# -------------------------


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = "__all__"


class ImagenForm(forms.ModelForm):
    imagen = forms.ImageField(
        label="Imagen",
        widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}),
    )

    class Meta:
        model = Imagen
        fields = ("imagen",)
