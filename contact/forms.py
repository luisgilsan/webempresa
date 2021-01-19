from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre",required=True,widget=forms.TextInput(
        attrs={'class':'form-control'}
    ),min_length=8,max_length=100)
    email = forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'email@ejemplo.com'}
    ),min_length=8,max_length=100)
    content = forms.CharField(label="Contenido",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':'Esbribe tu mensaje'}
    ),min_length=12,max_length=255)