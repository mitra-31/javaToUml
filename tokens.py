

import re


###########################################################
#     Lexer   
###########################################################
class Lexer:

    def __init__(self,code):
        self.code = code
        self.code_sp = code.split('\n')
        self.code_class = code.split('class')
        self.className = {}
        self.classnameReg = r'\b((?:public class|class|private class)\s*\w+)'
        self.classnameReg1 = r'\b((?:public class|class|private class)\s*\w+\s+extends\s*\w+)'
        self.methodsReg = r"\b((?:void|int|long|String|float)\s+\w+\s*\(\)).?"
        self.variablesReg = r"\b((?:int|Long|String|float)\s*\w+)"
        self.variablesReg1 = r"\b((?:int|Long|String|float)\s*\w+(?:\,\w+){1,})"
        self.Class()
        self.methods()
        self.variables()

    
    def Class(self):
        inherit = None       
        line1 = re.findall(self.classnameReg,self.code)
        line2 = re.findall(self.classnameReg1,self.code)
        for line_lst in line1+line2:
            line_lst = line_lst.split()
            # First Lets check the Access Modifiers of the class
            Modifier =  [line_lst[i] for i in range(len(line_lst)) if line_lst[i] == "private" or line_lst[i] == 'protected']
            classAccess = Modifier[0] if Modifier else 'public'
            # Removing Modifiers.
            line_lst = [i for i in line_lst if i not in ["public","class","private",'protected']]
            # After removing Modifiers first word in list will be the class name.
            classname = line_lst[0]
            # Now Lets check whether the class is Base class or Inherited one.
            #print(line_lst)
            extend_class = [line_lst[i+1] for i in range(len(line_lst)) if line_lst[i] == 'extends']
            
            inherit =  extend_class[0] if extend_class else 'Base'
            self.className[classname] = {'classname' : classname,'modifier' : classAccess,"Inherited":inherit,"class Variables":[],"class methods":[]}
        return 

        
  


    def methods(self):
        classes = self.className.keys()
        for code in self.code_class:
            if code.strip().split()[0] in classes:
                classname = code.strip().split()[0]
                methods = re.findall(self.methodsReg,code)
                self.className[classname]['class methods'].extend(methods)
        return
    
    def variables(self):
        classes = self.className.keys()
        for code in self.code_class:
            if code.strip().split()[0] in classes:
                classname = code.strip().split()[0]
                variables = re.findall(self.variablesReg,code)
                variables1 = re.findall(self.variablesReg1,code)
                if variables1:
                    for var in variables1:
                        var = var.split(",")
                        dataType = var[0].split()[0]
                    variables1 = [dataType+" "+i for i in var[1:]]
                self.className[classname]['class Variables'].extend(variables+variables1)
        return

    
    def display(self):
        import json
        print(json.dumps(self.className,indent=4))

    def classDict(self):
        return self.className


