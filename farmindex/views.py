# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'index.html')
	#return HttpResponse("Welcome to Farm Buddy!")



# Create your views here.
