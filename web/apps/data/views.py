from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from BeautifulSoup import BeautifulSoup
import mechanize 
import urllib

def tmp(request):
	appliances = [] 
	appliances.append("Fridge")
	appliances.append("Heater")
	appliances.append("Dish Washer")
	appliances.append("Toaster")

	user_data = [5000,4000,6000]
	average_data = [4500,4500,7000]
	return render_to_response("main.html",{"appliances":appliances,"user_data":user_data,"average_data":average_data},context_instance=RequestContext(request))

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
