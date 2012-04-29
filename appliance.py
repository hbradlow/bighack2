class Appliance:

    def __init__(self, name):
        """
        Initialize the Appliance with a string name, which will be used to import the relevant data from a json file
        """
        from json import loads
        f = open(str(name)+".json", 'r')
        self.database = loads(f.readline())
        f.close()

    def getModel(self, modelnumber):
        """
        Return a dictionary containing all the information for the given model.
        """
        return self.database[modelnumber]

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
        Return a list of the available filter parameters for this device
        """
        from random import choice
        k = choice(self.database.keys())
        return [x for x in self.database[k]]

    def get
    
