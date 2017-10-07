# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'farmindex/index.html')

def fetch(request):
	return render(request, 'farmindex/index_pre.html')

def landlord(request):
	return render(request, 'farmindex/landlord.html')

def household(request):
	return render(request, 'farmindex/household.html')

def wells(request):
	return render(request, 'farmindex/wells.html')

def mainpage(request):
	return render(request, 'farmindex/mainpage.html')




# Create your views here.
