import csv
from models import Fridge, Appliance

f = open('fridge.csv')
data = csv.reader(f) 
f.next() 

for row in data:
    try:
        brand = row[2]
    except:
        brand = ""
    try: 
        manufacturer = row[1]
    except:
        manufacturer = ""
    try:
        model = row[3]
    except:
        model = "" 
    try: 
        style = row[4]
    except: 
        style = "" 
    try: 
        defrost = row[5]
    except: 
        defrost = "" 
    try: 
        fridge  = row[6]
    except: 
        fridge  = "" 
    try: 
        accessory = row[7]
    except: 
        accessory = "" 
    try: 
        anti_sweat = row[8] 
    except: 
        anti_sweat = "" 
    try: 
        f_type = row[9] 
    except: 
        f_type = "" 
    try: 
        fresh_food = float(row[10])
    except: 
        fresh_food = 0.0
    try: 
        freezer_vol = float(row[11])
    except: 
        freezer_vol = 0.0
    try:
        total_vol = float(row[12])
    except: 
        total_vol = 0.0
    try:
        height = float(row[13])
    except: 
        height = 0.0 
    try: 
        width = float(row[14])
    except: 
        width = 0.0 
    try: 
        depth = float(row[15])
    except: 
        depth = 0.0 
    try:
        energy = float(row[16])
    except: 
        energy = 99999999999.9

    app = Appliance(manufacturer=manufacturer, brand = brand, model = model, annual_energy_consumption = energy)
    app.save()
    fridge = Fridge(appliance = app, style = style, defrost=defrost, fridge_type = f_type, access = accessory, fresh_volume = fresh_food, freezer_volume = freezer_vol, total_volume = total_vol, width = width, height = height, depth = depth)
    fridge.save()
