from analyzer import *

import re


###########################################################
#     Lexer   
###########################################################
class Lexer:

    def __init__(self,code):
        self.code = code
        self.code_sp = code.split('\n')
        self.code_class = code.split('class')
        self.len_ = len(self.code_sp)
        self.className = {}
        self.pos = -1
        self.current_line = None 
        self.move()
        self.make_tokens()


    def move(self):
        self.pos +=1
        self.current_line = self.pos if self.pos < self.len_ else None

    def Class(self):
        count = 1
        while self.current_line != None:
            line = self.code_sp[self.current_line]
            x = DefineToken(line).token()
            if x:
                self.className[count] = x
                print(x)
                count += 1
            self.move()
        #print(self.className)
        return 

        
    def Methods(self):
        pass

    def make_tokens(self):
        self.Class()
         


