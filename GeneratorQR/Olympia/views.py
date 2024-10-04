from http.client import responses
from pkgutil import get_data
from sysconfig import get_path

from django.contrib.staticfiles.utils import get_files
from django.core.handlers.wsgi import get_path_info
from django.shortcuts import render
from django.http import HttpResponse
import json
from tkinter import messagebox


def home(response):
    return render(response, 'homepage.html', {})

def guide(response):
    return render(response, 'guide.html', {})

def qrdata(response):
    return render(response, 'qrdata.html', {})

def code(response):
    return render(response, 'qrcode.html', 
