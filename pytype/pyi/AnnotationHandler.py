

class AnnotationHandler:


    __instance = None
    
    annot = list

    def getInstance():
      """ Static access method. """
      if AnnotationHandler.__instance == None:
         AnnotationHandler()
      return AnnotationHandler.__instance
    def __init__(self):
      """ Virtually private constructor. """
      if AnnotationHandler.__instance != None:
         raise Exception("This class is a singleton!")
      else:
        self.annot = []
        AnnotationHandler.__instance = self

    def add_annotation(self,annotation):
        
        self.annot.append(annotation)


    def get_annotation(self):
        return self.annot

