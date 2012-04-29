from appliance import Appliance
from random import choice

app = Appliance('heater')
params = app.getParameters()
choices = [choice(params.keys()) for i in range(10)]
for x in choices:
    print x
    print params[x]
