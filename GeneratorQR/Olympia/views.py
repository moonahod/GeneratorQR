from http.client import responses
from pkgutil import get_data
from sysconfig import get_path

from django.contrib.staticfiles.utils import get_files
from django.core.handlers.wsgi import get_path_info
from django.shortcuts import render
from django.http import HttpResponse
import tkinter
import json
from tkinter import *
from tkinter import messagebox


def home(request):
    return render(request, 'homepage.html')

def guide(request):
    return render(request, 'guide.html')

def start(request):
    return render(request, 'qrdata.html')

def code(request):
    return render(request, 'qrcode.html')