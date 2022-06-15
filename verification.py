from pytype.pyi.AnnotationHandler import AnnotationHandler
from z3 import *
ZVar = z3.RealSort()
class Verification:

    def __init__(self):
        self.vars = {}
        self.annotations = []
        self.anHandler = AnnotationHandler.getInstance()
        self.solver = Solver()
    def check_node(self,node):
        newAnot = self.anHandler.get_annotation()


        if not node.aliases == ():
            for al in node.aliases:
                self.vars[al.name] = z3.Const(al.name,ZVar)
                print(f"{al.name} added as const")
                self.vars[al.type.name] = z3.Const(al.name,ZVar)
                print(f"{al.type.name} added as const")
                self.solver.add(self.vars[al.name] == self.vars[al.type.name])
                print(f"{al.name} == {al.type.name}")
                

            for newAn in newAnot:
                if newAn not in self.annotations:
                    self.annotations.append(newAn)

                    for var in self.vars.keys():
                        for an in newAn:
                            print(f"{var} in {an} ?")
                            if an.__contains__(var):
                                print("var = {var}")
                                locals()[var] = self.vars[var]
                                print(f"{an} an added to solver")
                                self.solver.add(eval(an))
                                print(self.solver.check())
                    #print(self.solver.model())



        
        
