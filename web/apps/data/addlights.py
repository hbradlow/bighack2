from csv import reader
from data.models import FlourescentLamp,Appliance

f = reader(open('lights.csv'))
f.next()


for row in f:
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
        int(annual_energy_consumption=row[8])
    except:
        annual_energy_consumption=-1
    app = Appliance(manufacturer=manufacturer,brand=brand,model=model,annual_energy_consumption=annual_energy_consumption)
    app.save()

    light = FlourescentLamp(appliance=app)
    light.save()

