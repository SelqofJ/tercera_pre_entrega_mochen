from django import forms


class FormularioCliente(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(required=True, max_length=256)
    comentarios = forms.TextInput()


"""cantidad = forms.IntegerField(required=True, max_value=100)
    estado = forms.CharField(max_length=64)"""