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
        self.funcContext = run_prelude()
        VerificationHandler.__instance = self

    def run_verification(self, line):
        verif.verify_lines(line, self.context, self.funcContext, solver=self.solver)