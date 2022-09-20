from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.shortcuts import render
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def Newsletter_SignUp(request): #Enviamos correo electronico
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists(): #En caso de que el mail ya este registrado
            messages.warning(request, 'Este email ya se encuentra registrado')

        else: #En caso contrario guardamos el mail y enviamos correo
            instance.save()
            messages.success(request, 'Hemos enviado un mail a tu correo, revisa la casilla de spam')
            subject = "Bienvenido a rutasdev"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            html_template = 'newsletters/email/welcome.html'
            html_message = render_to_string(html_template)
            message = EmailMessage(subject,html_message,from_email,to_email)
            message.content_subtype = 'html'
            message.send()

    context = {
        'form':form,
    }
    
    return render(request, 'start.html', context)


def Newsletter_Unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.Success(request, 'Has anulado tu suscripcion, muchas gracias')

        else:
            print('Email no encontrado')
            messages.Warning(request, 'El correo no ha sido encontrado')

    context = {
        'form':form
    }
    
    return render(request, 'unsubscribe.html', context)