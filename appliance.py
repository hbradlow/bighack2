class Appliance:

    def __init__(self, name):
        """
        Initialize the Appliance with a string name, which will be used to import the relevant data from a json file
        """
        from json import loads
        f = open(str(name)+".json", 'r')
        self.database = loads(f.readline())
        self.parameterValues = self.database['parameterValues']
        self.database['parameterValues'] = {}
        f.close()

    def getModel(self, modelNumber):
        """
        Return a dictionary containing all the information for the given model.
        """
        return self.database[modelNumber]

    def filterBy(self, parameters):
        """
        return a dictionary of appliances, filtered by the parameters of the form {param:value}
        """
        result = {}
        for appliance in self.database:
            flag = False
            for param,value in parameters.items():
                if self.database[appliance][param] != value:
                    flag = True
                    break
            if not flag:
                result[appliance] = self.database[appliance]
        return result

    def getParameters(self):
        """
        Return a dictionary of the form {'parameter' : [val1, val2, ...]}
        """
        return self.parameterValues

    def upgrade(self, modelNumber, filters={}, k=10):
        """
        Return a list  of the k best substitutes for the appliance filtered to contain only appliances matching the given filters
        filters is a list of parameters
        """
        currentModel = self.getModel(modelNumber)
        filterDict = {}
        for param in filters:
            filterDict[param] = currentModel[param]
        filteredApps = self.filterBy(filterDict)
        filteredList = [(app['energy_consumption'], app) for app in filteredApps]
        return filteredList.sorted()[:k]
