import re
import token

class DefineToken:

    def __init__(self,line):
        self.line = line
        self.Dict = {}
        self.classnames = []
        self.delimiters = [" ",";","="]
        self.classname = r'^public class\s*\w+|class\s*\w+|private class\s*\w+'
        self.dataTypes = ['String','int','long','boolean','float','short','char']
        self.variables = ['{}\s+\w+'.format(i) for i in self.dataTypes]

    def removeDelimiters(self,line):
        string = [i for i in line if i not in ["\t",'{',';']]
        return "".join(string)
        
    def token(self):
        
        line = self.removeDelimiters(self.line)
        
        #================================================================================
        # To check classes, Syntax of class 'public class class_name' or 'class class_name.
        # We need to even check wether the class is base or the class has being inherited. 
        #================================================================================
        
        if re.match(self.classname,line):
            name = self.className(line) 

            return name
        return


    def Methods(self,line_lst):
        pass
         
    
    def className(self,line):

        line_lst = line.split(" ")
        # First Lets check the Access Modifiers of the class
        Modifier =  [line_lst[i] for i in range(len(line_lst)) if line_lst[i] == "private" or line_lst[i] == 'protected']
        classAccess = Modifier[0] if Modifier else 'public'
        
        # Removing Modifiers.
        line_lst = [i for i in line_lst if i not in ["public","class","private",'protected']]
        
        # After removing Modifiers first word in list will be the class name.
        classname = line_lst[0]

        # Now Lets check whether the class is Base class or Inherited one.
        extend_class = [str(line_lst[i+1]) for i in range(len(line_lst)) if line_lst[i] == "extends"]
        inherit = extend_class[0] if extend_class  else "Base"

        return {'classname' : classname,'modifier' : classAccess,"Inherited":inherit,"class Variables":{},"class methods":{}}


######################################################
# {
#   class :       
#            { 
#               classname : student
#               Inhertited : Base
#               classVariables :
#                               {    
#                                   string : usn
#                                   string : name
#                                   string : branch
#                                   long : phone
#                               }   
#               classMethods : 
#                             { 
#                                void : read(void)
#                                void : print(void)
#                             } 
#            }
#   }
############################################################