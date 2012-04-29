from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from BeautifulSoup import BeautifulSoup
import mechanize 
import urllib
from data.models import *
from data.ecost import *

def tmp(request):
	appliances = [] 

	user_data = []
	average_data = []

	import random
	line_data_x = sum_cost(Appliance.objects.all()[0])[0] 
	line_data_y = sum_cost(Appliance.objects.all()[1])[0] 
	return render_to_response("main.html",{"appliances":appliances,"user_data":user_data,"average_data":average_data,"line_data_x":line_data_x,"line_data_y":line_data_y},context_instance=RequestContext(request))

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
	appliances = Appliance.objects.filter(brand__icontains=request.POST["query"])[:10]
	return HttpResponse(json.dumps([str(a) for a in appliances]))

def ajax_appliance_curve(request):
	import json
	a = Appliance.objects.get(pk=request.POST['pk'])
	line_data_x = sum_cost(a)[0]
	return HttpResponse(json.dumps({"data":line_data_x,"name":str(a)}))

