import csv
from models import Appliance, Heater, Fridge

f = open('heater.csv')
data = csv.reader(f)
f.next()

for row in data:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = 0
    try:
        manufacturer=row[1]
    except:
        manufacturer=None
    try: 
        brand=row[2]
    except:
        brand=None
    try: 
        model=row[3]
    except:
        model = None
    try: 
        int(annual_energy_consumption=row[27])
    except:
        annual_energy_consumption=100000
    app = Appliance(manufacturer=manufacturer,brand=brand,model=model,annual_energy_consumption=annual_energy_consumption)
    app.save()
    try:
        boiler_type=row[4]
    except:
        boiler_type = None
    try: 
        burner_type=row[6]
    except:
        burner_type=None
    try: 
        energy_source=row[5]
    except:
        energy_source=None
    try: 
        pilot_light=row[7]
    except:
        pilot_light = None
    try:
        outdoor=row[8]
    except:
        outdoor = False
    try: 
        flue_gas=row[12]
    except:
        flue_gas = None
    try: 
        control=row[13]
    except:
        control = None
    try:
        boiler_design=row[14]
    except:
        boiler_design = None
    try:
        appliance=app
    except:
        appliance = None
    heater = Heater(boiler_type=boiler_type,burner_type=burner_type,energy_source=energy_source,pilot_light=pilot_light,outdoor=outdoor,flue_gas=flue_gas,control=control,boiler_design=boiler_design,appliance=appliance)
    heater.save()
