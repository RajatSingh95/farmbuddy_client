# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# It renders the landing Page of the website.
def index(request):
	return render(request, 'farmindex/landingpages/index.html')

def login(request):
	if request.method == 'POST':
		mobile = request.POST.get('mobile', None)
		password = request.POST.get('password', None)
		credentials={'mobile':mobile, 'pass': password}
		print credentials

def fetch(request):
	return render(request, 'farmindex/index_pre.html')

# this view is for farm Page with Google Maps
def landlord(request):
	return render(request, 'farmindex/landlord.html')

# This view is for all the houses on the map with their details.
def household(request):
	return render(request, 'farmindex/household.html')

# This view is for all the wells on the map with their details.
def wells(request):
	return render(request, 'farmindex/wells.html')

# This renders the main Page after logging in to the portal.
def mainpage(request):
	return render(request, 'farmindex/mainpage.html')




# Create your views here.
