# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# It renders the landing Page of the website.
def index(request):
	return render(request, 'farmindex/landingpages/index.html')

def login(request):
	if request.method == 'POST':
		mobile = request.POST.get('mobile', None)
		password = request.POST.get('password', None)
		credentials={'mobile':mobile, 'pass': password}
		response = requests.post('http://10.0.3.23:8017/restapi/logindetail/', data=credentials)
		print(response)
		print(response.content)
		jsonr=response.content
		json_dec=jsonr.decode("utf-8")
		print(json_dec)
		json_res=json.loads(json_dec)
		print(json_res['login'])
		if json_res['login']=="success":
			return render(request, 'farmindex/mainpage.html')
		print(json_res['login'])
		print(credentials)


def statistics(request):
	##################
	analytics={'type': 'Rice'}
	response = requests.post('http://10.0.3.23:8017/restapi/statistic/', data=analytics)
	jsonr=response.content
	json_dec=jsonr.decode("utf-8")
	json_res=json.loads(json_dec)
	lst=[]
	dic={}
	for obj in json.loads(json_res['crop_detail']):
		if obj['fields']['Year'] in dic:
			dic[obj['fields']['Year']]+=obj['fields']['Yield']
		else:
			dic[obj['fields']['Year']]=obj['fields']['Yield']
		print(obj['fields']['Name'])
	for year in dic:
		dt={}
		dt['x']=year
		dt['y']=dic[year]
		lst.append(dt)
	print(lst)
	print(dic)
	print(json_res)
	###################
	analytics={'type': 'Wells'}
	response = requests.post('http://10.0.3.23:8017/restapi/statistic/', data=analytics)
	jsonr=response.content
	json_dec=jsonr.decode("utf-8")
	json_res=json.loads(json_dec)
	lst2=[]
	dic={}
	area_count={}
	for obj in json.loads(json_res['well_detail']):
		if obj['fields']['Area'] in dic:
			dic[obj['fields']['Area']]+=obj['fields']['depth']
			area_count[obj['fields']['Area']]+=1
		else:
			dic[obj['fields']['Area']]=obj['fields']['depth']
			area_count[obj['fields']['Area']]=1
		print(obj['fields']['Area'])
	for key in dic:
		dic[key]=(dic[key])/area_count[key]
	for area in dic:
		dt={}
		dt['y']=dic[area]
		dt['label']=area
		lst2.append(dt)
	print(lst2)
	print(dic)
	print(json_res)
	#######################

	analytics={'type': 'Income'}
	response = requests.post('http://10.0.3.23:8017/restapi/statistic/', data=analytics)
	jsonr=response.content
	json_dec=jsonr.decode("utf-8")
	json_res=json.loads(json_dec)
	lst3=[]
	dic={}
	dic['below 20k']=0
	dic['between 20k-50k']=0
	dic['between 50k-75k']=0
	dic['between 75k-100k']=0
	dic['above 1lac']=0
	house_count={}
	house_count['below 20k']=0
	house_count['between 20k-50k']=0
	house_count['between 50k-75k']=0
	house_count['between 75k-100k']=0
	house_count['above 1lac']=0
	for obj in json.loads(json_res['house_detail']):
		if obj['fields']['Income'] < 20000:
			dic['below 20k']+=obj['fields']['Income']
			house_count['below 20k']+=1
		elif obj['fields']['Income'] > 20000 and obj['fields']['Income'] < 50000:
			dic['between 20k-50k']+=obj['fields']['Income']
			house_count['between 20k-50k']+=1
		elif obj['fields']['Income'] > 50000 and obj['fields']['Income'] < 75000:
			dic['between 50k-75k']+=obj['fields']['Income']
			house_count['between 50k-75k']+=1
		elif obj['fields']['Income'] > 75000 and obj['fields']['Income'] < 100000:
			dic['between 75k-100k']+=obj['fields']['Income']
			house_count['between 75k-100k']+=1
		elif obj['fields']['Income'] > 100000:
			dic['above 1lac']+=obj['fields']['Income']
			house_count['above 1lac']+=1
		print(obj['fields']['Income'])
	for key in dic:
		dic[key]=(dic[key])/(house_count[key]+1)
	for cat in dic:
		dt={}
		dt['y']=house_count[cat]
		dt['label']=cat
		lst3.append(dt)
	print(lst3)
	print(dic)
	print(json_res)
	#####################

	analytics={'type': 'Family'}
	response = requests.post('http://10.0.3.23:8017/restapi/statistic/', data=analytics)
	jsonr=response.content
	json_dec=jsonr.decode("utf-8")
	json_res=json.loads(json_dec)
	lst4=[]
	dic={}
	family_count={}
	for obj in json.loads(json_res['family_detail']):
		if obj['fields']['Members'] in dic:
			dic[obj['fields']['Members']]+=obj['fields']['Income']
			family_count[obj['fields']['Members']]+=1
		else:
			dic[obj['fields']['Members']]=obj['fields']['Income']
			family_count[obj['fields']['Members']]=1
		print(obj['fields']['Members'])
	for key in dic:
		dic[key]=(dic[key])/family_count[key]
	for mem in dic:
		dt={}
		dt['x']=mem
		dt['y']=dic[mem]
		lst4.append(dt)
	print(lst4)
	print(dic)
	print(json_res)
	
	data={'rice': lst , 'well':lst2, 'income':lst3, 'family':lst4}
	return render(request, 'farmindex/statistics.html',data)

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
