import os

def parser_comments(file):

        folder = "./../ros_verification/ROSMessagesAnnotated"
        result = []
        caminho = f"{folder}/{file}.msg"
        print(caminho)
        if os.path.isfile(caminho) :
                print("é ficheiro")
                readFile = open(caminho, "r")

                lines = readFile.readlines()

                specLines = []

                for line in lines:
                        if line.__contains__("#RobotFix#"):
                                splitLine = line.split("#RobotFix#")
                                for sLine in splitLine[1:]:
                                        specLines.append(sLine)
                                        rLine = sLine.replace(")","(")
                                        rsLine = rLine.split("(")
                                        index = 0
                                        print(rsLine)
                                        for rsPart in rsLine:
                                                if rsPart.__contains__("Unit"):
                                                        unitSplit = rsLine[index+1].split(",")
                                                        result += [("Unit",(unitSplit[0],unitSplit[1]))]
                                                if rsPart.__contains__("Annotation"):
                                                        result += [("Annotation",rsLine[index+1])]
                                                index += 1  
        else:
                print("não é ficheiro")
        return result



print(parser_comments("Twist"))