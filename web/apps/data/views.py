from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from BeautifulSoup import BeautifulSoup
import mechanize 
import urllib
from data.models import *

def tmp(request):
	appliances = [] 
	appliances.append("Fridge")
	appliances.append("Heater")
	appliances.append("Dish Washer")
	appliances.append("Toaster")

	user_data = [5000,4000,6000,1000]
	average_data = [4500,4500,7000,1000]
	return render_to_response("main.html",{"appliances":appliances,"user_data":user_data,"average_data":average_data},context_instance=RequestContext(request))

def collect_fn(unit_type, unit_nr):

    br = mechanize.Browser()
    br.open("http://amazon.com") 
    br.select_form(name="site-search") 
    br['field-keywords'] = unit_type + " " + unit_nr
    response = br.submit()
    soup = BeautifulSoup(response.read())
    return str(soup.find("div", {"id" : "result_0"})) 

def collect(request):
    unit_type = request.GET["unit_type"]
    unit_nr = request.GET["unit_nr"]

    br = mechanize.Browser()
    br.open("http://amazon.com") 
    br.select_form(name="site-search") 
    br['field-keywords'] = unit_type + " " + unit_nr
    response = br.submit()
    soup = BeautifulSoup(response.read())
    return HttpResponse(str(soup.find("div", {"id" : "result_0"})))

def ajax_appliance(request):
	import json
	appliances = Appliance.objects.filter(brand__icontains=request.POST["query"])
	return HttpResponse(json.dumps([str(a) for a in appliances]))

def costOverTime(request):
    unit_type = request.GET['unit_type']
    unit_nr = request.GET['unit_nr']

def averageConsumption(request):
    unit_type = request.GET['unit_type']
    if unit_type == 'Heater':
        items = Heater.objects.all()
        totalUsage = 0.0
        for unit in items:
            totalUsage += unit.appliance.annual_energy_consumption
        return HttpResponse(str(totalUsage/len(items)))

    elif unit_type == 'Fridge':
        items = Fridge.objects.all()
        totalUsage = 0.0
        count = 0
        for unit in items:
            totalUsage += unit__appliance__annual_energy_consumption
        return HttpResponse(str(totalUsage/count))
    else:
        return HttpResponse("No such appliance")
    
