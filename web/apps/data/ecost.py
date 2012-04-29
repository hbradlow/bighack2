from models import Appliance

def sum_cost(appliance): 
    cost_day = appliance.annual_energy_consumption*0.127/365
    lst = []
    for i in range(365): 
        lst[i] = cost_day*(i+1)

    return lst
