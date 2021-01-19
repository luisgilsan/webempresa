from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Envio de correo
            to_send = EmailMessage(
                "Nueva petición EasyTrans",
                "De {} <{}> \n\nEscribió\n\n{}".format(name,email,content),
                "informacion@atlasrepuestos.com",
                ['luisgilsan_007@hotmail.com'],
                reply_to=[email]
            )
            try:
                to_send.send()
            except:
                return redirect(reverse('contact')+'?fail')

        return redirect(reverse('contact')+'?ok')

    return render(request,'contact/contact.html',{'form':contact_form})