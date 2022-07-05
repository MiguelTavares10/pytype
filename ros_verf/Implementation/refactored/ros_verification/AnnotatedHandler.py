import z3

class AnnotatedHandler:
    __instance = None
    
    def getInstance():
      """ Static access method. """
      if AnnotatedHandler.__instance == None:
         AnnotatedHandler()
      return AnnotatedHandler.__instance
    def __init__(self):
      """ Virtually private constructor. """
      if AnnotatedHandler.__instance != None:
         raise Exception("This class is a singleton!")
      else:
        self.annot_vars = []
        self.annot_message = []
        AnnotatedHandler.__instance = self

    def add_var_annotated(self,name):
        
        self.annot_vars.append(name)


    def get_var_annotated(self):
        return self.annot_vars


    def var_is_annotated(self,name):
        return name in self.annot_vars


    def add_message_annotated(self,name):
        self.annot_message.append(name)

    def get_message_annotated(self):
        return self.annot_message

    def message_is_annotated(self,name):
        return name in self.annot_message