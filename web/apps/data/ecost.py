from models import Appliance
from amazon import collect 
from BeautifulSoup import BeautifulSoup
def sum_cost(appliance): 
    cost_day = appliance.annual_energy_consumption*0.127/365
    lst = []
    for i in range(365): 
        lst[i] = cost_day*(i+1)
    result = collect(appliance.model, appliance.brand)
    soup = BeautifulSoup(result)
    price = soup.find("span", {"class" : "price addon"}).text
    return [lst, result, price]
