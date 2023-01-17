from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    apellido = forms.CharField(required=True, max_length=256)
    dni = forms.CharField(required=True,max_length=64)
    email = forms.EmailField(required=True)
    fecha_nac = forms.DateField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)

class ComentarioFormulario(forms.Form):
    comments = forms.CharField(required=True, max_length=256)
 
