import os
import time
from io import StringIO

from threading import Thread

from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    """
    Método encargado de renderizar la página principal

    :param request: _description_
    :type request: _type_
    :return: _description_
    :rtype: _type_
    """
    status = "*"
    context={"status": status}
    return render(request, 'dashboard.html', context=context)

