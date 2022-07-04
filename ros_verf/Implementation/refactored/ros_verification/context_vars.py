class GlobalContext:
        def __init__(self, name, gblData = "None"):
                self.name = name
                self.iteration = 0
                self.instances = []
                firstInstance = InstanceContext(name)
                self.instances.append(firstInstance)
                self.lastInstance = firstInstance
                self.globalData = []
                if not gblData == "None":
                        self.globalData.append(gblData)
                self.global_unit = {}
                self.datatype = "None"


        def add_instance(self, data = ""):
                self.iteration += 1
                instance = InstanceContext(self.name+"_"+str(self.iteration))
                self.instances.append(instance)
                self.lastInstance = instance
                return self.lastInstance.get_name()

        def get_last_instance(self):
                return self.lastInstance

        def add_global_data(self, data):
                self.globalData.append(data)

        def get_global_data(self):
               return self.globalData

        def add_global_unit(self,unit,name):
                self.global_unit[name] = unit
        
        def get_global_unit(self,name):
                return self.global_unit[name]

        def add_datatype(self,datatype):
                self.datatype = datatype

        def get_datatype(self):
                return self.datatype
class InstanceContext:
        def __init__(self, name):
                self.name = name
                self.data = {}

        def get_name(self):
                return self.name

        def get_data(self,name):
                if self.in_data_context(name):
                        return self.data[name]
                else:
                        return ""

        def add_data(self,data,name): 
                self.data[name] = data

        def in_data_context(self,name):
                return name in self.data




