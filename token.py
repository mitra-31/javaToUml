
class Position:

    def __init__(self,idx,ln,col):
        self.idx = idx
        self.ln = ln
        self.col = col

    def move(self,current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0
        return self
        
    def copy(self):
        return Position(self.idx,self.ln,self.col)

###########################################################
#     Lexer   
###########################################################


class Lexer:

    def __init__(self,code):
        self.code = code
        self.len = len(self.code)
        self.pos = Position(-1,0,-1)
        self.current_char = None
        self.move()

    def move(self):
        self.pos.move(self.current_char)
        self.current_char = self.code[self.pos.idx] if self.pos.idx < self.len else None

    
    def make_tokens(self):

        tokens = []
        present_idx = 0

        while self.current_char != None:

            if self.current_char == "\t":
                self.move()
            else:
                
                if self.move():
                    tok = self.code[present_idx:self.pos.idx].strip()
                    tokens.append(tok)
                self.move()
        return tokens
     