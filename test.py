from appliance import Appliance
from random import choice

app = Appliance('heater')
k = choice(app.getParameters)
print app.filterBy({
