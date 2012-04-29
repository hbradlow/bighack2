import csv, json

applianceReference = {'fridge' : 'fridges.csv', 'heater' : 'heaters.csv'}

for applianceName in applianceReference:
    appliances = csv.reader(open(applianceReference[applianceName]))
    header = appliances.next()
    applianceDict = {}
    parameterValues = {}
    for h in header:
        parameterValues[h] = set()
    for row in appliances:
        applianceDict[row[3]] = {}
        for k,v in zip(header,row):
            applianceDict[row[3]][k] = v
            parameterValues[k].add(v)
    for p in parameterValues:
        parameterValues[p] = list(parameterValues[p])
    applianceDict['parameterValues'] = parameterValues
    f = open(applianceName+".json", 'w')
    f.write(json.dumps(applianceDict))
    f.close()
    print "wrote " + applianceName
