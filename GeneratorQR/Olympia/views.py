from http.client import responses
from lib2to3.fixes.fix_input import context
from os.path import pathsep
from pkgutil import get_data
from sysconfig import get_path

from django.contrib.staticfiles.utils import get_files
from django.core.handlers.wsgi import get_path_info
from django.shortcuts import render, redirect
import qrcode
from PIL import ImageTk, Image
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from qrcode.console_scripts import error_correction
from typing_extensions import final


def home(request):
    render(request, 'homepage.html')
    viaggio = 1
    if request.method == 'POST':
        data = request.POST.get('qrdata')
        print('data to code: ', data)
        filename = request.POST.get('filename')
        print('filename: ', filename)
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        type(img)
        fileFormat = request.POST.get('fileFormat')
        name = (filename + fileFormat)
        finalcode = img.save('../GeneratorQR/Olympia/static/codes/' + name)
        path = ('/static/codes/' + name)
        context = {
            'code1': path,
            'data_check': len('code1') > 10,
        }
        return render(request, 'homepage.html', context)
    else:
        return render(request, 'homepage.html')

#def code(response):
    #return render(response, 'homepage.html')
