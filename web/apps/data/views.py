from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

def tmp(request):
	appliances = [] 
	appliances.append("Fridge")
	appliances.append("Heater")
	appliances.append("Dish Washer")
	appliances.append("Toaster")

	user_data = [5000,4000,6000]
	average_data = [4500,4500,7000]
	return render_to_response("main.html",{"appliances":appliances,"user_data":user_data,"average_data":average_data},context_instance=RequestContext(request))
