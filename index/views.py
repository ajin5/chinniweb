from django.http import HttpResponse
from django.shortcuts import render
from .models import contactform
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html' )

@csrf_exempt
def contacts(request):
    if request .method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactformdata = contactform(name = name, email = email, subject = subject, message = message)
        contactformdata.save()
    return render(request, 'contacts.html')
       
