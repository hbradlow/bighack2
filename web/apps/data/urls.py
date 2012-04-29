from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("data.views",
		url("^ajax/amazon/$", "collect",name="amazon_collect"),
		url("^ajax/appliance/$", "ajax_appliance",name="ajax_appliance"),
)
