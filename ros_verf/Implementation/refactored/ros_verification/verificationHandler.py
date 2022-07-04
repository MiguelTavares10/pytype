import ros_verf.Implementation.refactored.ros_verification.verification as verif
import z3
from ros_verf.Implementation.refactored.ros_verification.run_prelude import run_prelude
class VerificationHandler:
    __instance = None
    
    def getInstance():
      """ Static access method. """
      if VerificationHandler.__instance == None:
         VerificationHandler()
      return VerificationHandler.__instance
    def __init__(self):
      """ Virtually private constructor. """
      if VerificationHandler.__instance != None:
         raise Exception("This class is a singleton!")
      else:
        self.context = verif.build_initial_context()
        self.solver = z3.Solver()
        self.annot_vars = []
        self.funcContext = run_prelude()
        VerificationHandler.__instance = self

    def add_var_annotated(self,name):
        
        self.annot_vars.append(name)


    def get_var_annotated(self):
        return self.annot_vars


    def var_is_annotated(self,name):
        if name in self.annot_vars:
            return True
        else:
            return False

    def run_verification(self, line):
        verif.verify_lines(line, self.context, self.funcContext, solver=self.solver)