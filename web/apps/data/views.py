from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from BeautifulSoup import BeautifulSoup
import mechanize 
import urllib
<<<<<<< HEAD
=======
from data.models import *
from data.ecost import *
>>>>>>> 0091916457402bf541f1e8c1cef6ab8c53f6ed58

def tmp(request):
	appliances = [] 
	appliances.append("Fridge")
	appliances.append("Heater")
	appliances.append("Dish Washer")
	appliances.append("Toaster")

<<<<<<< HEAD
	user_data = [5000,4000,6000,1000]
	average_data = [4500,4500,7000,1000]
	return render_to_response("main.html",{"appliances":appliances,"user_data":user_data,"average_data":average_data},context_instance=RequestContext(request))
=======
	user_data = []
	average_data = []

	import random
	line_data_x = []
	line_data_y = []
	return render_to_response("main.html",{"fridge_ave":1000,"heater_ave":2000,"appliances":appliances,"user_data":user_data,"average_data":average_data,"line_data_x":line_data_x,"line_data_y":line_data_y},context_instance=RequestContext(request))
>>>>>>> 0091916457402bf541f1e8c1cef6ab8c53f6ed58

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
<<<<<<< HEAD
=======

def ajax_appliance(request):
	import json
	appliances = Appliance.objects.filter(brand__icontains=request.POST["query"])[:10]
	return HttpResponse(json.dumps([str(a) for a in appliances]))

def ajax_appliance_curve(request):
	import json
	a = Appliance.objects.get(pk=request.POST['pk'])
	line_data_x = sum_cost(a)[0]
	return HttpResponse(json.dumps({"data":line_data_x,"name":str(a)}))

def costOverTime(request):
    unit_type = request.GET['unit_type']
    unit_nr = request.GET['unit_nr']

def averageConsumption_method(unit_type):
    if unit_type == 'Heater':
        items = Heater.objects.all()
        totalUsage = 0.0
        for unit in items:
            totalUsage += unit.appliance.annual_energy_consumption
        return totalUsage/len(items)

    elif unit_type == 'Fridge':
        items = Fridge.objects.all()
        totalUsage = 0.0
        count = 0
        for unit in items:
            totalUsage += unit.appliance.annual_energy_consumption
        return totalUsage/count
    else:
        return "No such appliance"

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
>>>>>>> 0091916457402bf541f1e8c1cef6ab8c53f6ed58
