from django.shortcuts import render
from django.http import HttpResponse
from django.core.EMAIL import send_mail

# Create your views here.
from app.forms import *
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail(
                'registration',
                'thank you for registering',
                'lakshmidabbara08@gmail.com',
                [MUFDO.save()],
                fail_silently=True
            )
            return HttpResponse('registration is succesfull')
        else:
            return HttpResponse('Invalid')
    return render(request,'registration.html',d)