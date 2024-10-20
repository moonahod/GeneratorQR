from http.client import responses
from pkgutil import get_data
from sysconfig import get_path

from django.contrib.staticfiles.utils import get_files
from django.core.handlers.wsgi import get_path_info
from django.shortcuts import render, redirect
import qrcode
#from .models import Draft
from django.http import HttpResponse


def home(response):
    return render(response, 'homepage.html', {})

def guide(response):
    return render(response, 'guide.html', {})

#def qrdata(response):
#    return render(response, 'qrdata.html', {})

def qrdata(response):
    return render(response, 'qrdata.html', {})
    #if response.method == 'POST':
     #   data = response.POST.get('qrdata')
     #   qrdraft = Draft(data=qrdata)
    #return render(response, 'qrdata.html', {}), redirect('/code')
    #if form.is_valid():
    #    form.save()
    #return redirect('../code/')
    #return render(request, 'qrdata.html', {})

def gencode(request):
    if request.method == 'POST':
        data = request.POST.get('qrdata')
        #qr = qrcode.QRCode(

        #)
        #qr.make(fit=True)
        #code = qr.make_image()
        #code.save('1.png')

    return render(request, 'qrcode.html', {})

def code(response):
    return render(response, 'qrcode.html', {})
