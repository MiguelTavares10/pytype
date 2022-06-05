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
                self.vars[al.type.name] = z3.Const(al.name,ZVar)
                self.solver.add(self.vars[al.name] == self.vars[al.type.name])
                print(f"{al.name} == {al.type.name}")
                

            for newAn in newAnot:
                if newAn not in self.annotations:
                    self.annotations.append(newAn)

                    for var in self.vars.keys():
                        if newAn.__contains__(var):
                            locals()[var] = self.vars[var]
                    self.solver.add(eval(newAn))
                    print(self.solver.check())
                    #print(self.solver.model())



        
        
