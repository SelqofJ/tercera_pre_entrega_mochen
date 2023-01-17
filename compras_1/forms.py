from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(required=True, max_length=256)
    dni = forms.CharField(max_length=64)
    email = forms.EmailField()
    fecha_nac = forms.DateField()

