# EVANGELOS    BALLOS   4739 cse94739
# KONSTANTINOS GKIOULIS 4654 cse94654
import sys

#####  LEX  #####

# codes as global variables
# STATES          FINAL STATES        ERRORS
S_START = 0   ;   F_EOF   = 100   ;   E_EOF   = -1
S_DIG   = 1   ;   F_NUM   = 101   ;   E_ILCHR = -2
S_IDK   = 2   ;   F_IDK   = 102   ;   E_IEXCL = -3
S_HASH  = 3   ;   F_GROUP = 103   ;   E_NAV   = -4
S_REM   = 4   ;   F_DELIM = 104   ;   E_ILGBR = -5
S_EOC   = 5   ;   F_ASGN  = 105   ;   E_BDHSH = -6
S_LST   = 6   ;   F_RELOP = 106   ;   E_ILDOL = -7
S_GRT   = 7   ;   F_ADDOP = 107   ;   E_BDDIV = -8  
S_EQUAL = 8   ;   F_MULOP = 108   ;   E_BDASN = -9
S_DEQL  = 9   ;                       E_TEQL  = -10
S_DIFF  = 10
S_DIV   = 11

# state automation   empty   ,  char/_  ,  nums    ,  + or -  ,  *       ,  /       ,  <       ,  >       ,  !       ,  =       ,  :/,/;   ,  () or [],  {}      ,  #       ,  $       ,  EOF
stateAutomation = [[ S_START ,  S_IDK   ,  S_DIG   ,  F_ADDOP ,  F_MULOP ,  S_DIV   ,  S_LST   ,  S_GRT   ,  S_DIFF  ,  S_EQUAL ,  F_DELIM ,  F_GROUP ,  E_ILGBR ,  S_HASH  ,  E_ILDOL ,  F_EOF   ], # 0  -  Start
                   [ F_NUM   ,  E_NAV   ,  S_DIG   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  E_ILGBR ,  F_NUM   ,  F_NUM   ,  F_NUM   ], # 1  -  Dig
                   [ F_IDK   ,  S_IDK   ,  S_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  E_ILGBR ,  F_IDK   ,  F_IDK   ,  F_IDK   ], # 2  -  Idk
                   [ E_BDHSH ,  S_IDK   ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  F_GROUP ,  E_BDHSH ,  S_REM   ,  E_BDHSH ], # 3  -  Hashtag
                   [ S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_EOC   ,  S_REM   ,  E_EOF   ], # 4  -  Remove
                   [ S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_EOC   ,  S_START ,  E_EOF   ], # 5  -  Exit Comment
                   [ F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_LST   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ], # 6  -  Smaller than
                   [ F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_GRT   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ], # 7  -  Larger than
                   [ F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  S_DEQL  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ], # 8  -  Equals
                   [ F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  E_TEQL  ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ], # 9  -  Double equals
                   [ E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  F_RELOP ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ], # 10 -  Different than
                   [ E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  F_MULOP ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ]  # 11 -  Divide
                  ]

# lexic unit strings
lexicUnits = ["",
               "number",
               "idk",
               "group",
               "delimiter",
               "assignment",
               "relOperator",
               "addOperator",
               "mulOperator"
               ]

# error explanations
errors = ["Illegal EOF",
          "Illegal character",
          "Illegal !",
          "Variables cannot start with a number",
          "Illegal bracket",
          "Hashtags need to be followed by $ or brackets",
          "Illegal $",
          "/ can only be followed by another /",
          "Bad assign",
          "Triple equals is illegal"
          ]


# ERRORS
# -1  - solo char

class Token:
# properties : recognized \ _string , family , line_number
    def __init__(self, recognized_string , family , line_number):
        self.recognized_string = recognized_string
        self.family = family
        self.line_number = line_number

class Lex:
    def __init__(self, filename):
        self.file = open(filename, 'r') # Open file
        self.currentLine = 1
        self.token = None
        self.buffer = ' ' # this can be used to pass the last character read
                          # from the previous token to the next, in case it's needed

    # associates character to it's respective identifier code
    def charcode(self, char):
        if   (char == ' ' or char == '\n' or char == '\t'): # whitespace
            return 0
        elif ((char >= 'A' and char <= 'z' and char not in ['[','/',']','^','`']) or char in ['\"',"\'"]): # a to Z and _
            return 1
        elif (char >= '0' and char <= '9'): # 0 to 9
            return 2
        elif (char == '+' or  char == '-' ): # + or -
            return 3
        elif (char == '*'): # * 
            return 4
        elif (char == '/'): # /
            return 5
        elif (char == '<'): # <
            return 6
        elif (char == '>'): # >
            return 7
        elif (char == '!'): # !
            return 8
        elif (char == '='): # =
            return 9
        elif (char == ':' or char == ',' or char == ';'): # : or , or ;
            return 10
        elif (char == '(' or char == ')' or char == '[' or char == ']'): # ( or ) or [ or ]
            return 11
        elif (char == '{' or char == '}'): # { or }
            return 12
        elif (char == '#'): # #
            return 13
        elif (char == '$'): # $
            return 14
        elif (char == ''): # EOF
            return 15
        else:
            return -1

    
    def lex(self):
        string = ''
        state = S_START
        while (state >= 0 and state < 100):

            # if there's a character in the buffer, retrieve it and empty the buffer
            if (self.buffer == ''):
                char = self.file.read(1)
            else:
                char = self.buffer
                self.buffer = ''

            # count possible next lines
            if (char == '\n'):
                self.currentLine += 1
            
            # associate character with the respective identifier code
            code = self.charcode(char)
            # if character is legal, get next state, otherwise error
            if (code >= 0):
                state = stateAutomation[state][code]
            else:
                state = E_ILCHR

            # if state not start and character does not belong
            # to a next lectic unit, add it to the string.
            # Otherwise, add it to the buffer
            if(state == S_START):
                string = ''
            elif (state != F_NUM and state != F_IDK and state != F_ASGN and state != F_RELOP):
                string += char
            else:
                self.buffer = char
                if (char == '\n'):
                    self.currentLine -= 1
        
        # if code is an error, process it
        if (state < 0):
            print("ERROR: " + errors[state*(-1)-1] + " at line " + str(self.currentLine) + " !!")
            exit(-1)
        
        return Token(string, lexicUnits[state - 100], self.currentLine)

def testLex():

    # Create lex object
    lex = Lex(sys.argv[1])

    # Return next token
    tokens = []
    while True:
        lex.token = lex.lex()
        tokens.append(lex.token)
        if (lex.token.recognized_string == ''):
            del tokens[len(tokens)-1]
            # Close file
            lex.file.close
            break

    out = "recognized string      |  family       |  line number\n"
    for i in range(0, len(tokens)):
        tk = tokens[i]
        out += "\'" + tk.recognized_string + "\'" + ' '*(20-len(tk.recognized_string)) + " |  " + tk.family + ' '*(12-len(tk.family)) + " |  " + str(tk.line_number) + "\n"
    return out


out = open("lex.out", 'w')
out.write(testLex())
out.close()


#####  SYNTAX  #####

class Parser:

    def __init__(self):
        self.lexical_analyzer = Lex(sys.argv[1])

    def syntax_analyzer(self):
        self.token = self.getToken()
        self.startRule()
        print("Compiled successfully")
    
    def getToken(self):
        return self.lexical_analyzer.lex()
    
    def error(self, issue, line):
        print("ERROR: " + issue + " on line " + str(line))
        exit(-1)
    
    def startRule(self):
        self.def_main_part()
        self.call_main_part()
    
    def def_main_part(self):
        self.def_main_function()
        while (self.token.recognized_string == 'def'):
            self.def_main_function()
    
    def def_main_function(self):
        returns = True
        if (self.token.recognized_string == "def"):
            self.token = self.getToken()
            if (self.token.family == "idk"):
                self.token = self.getToken()
                if (self.token.recognized_string == "("):
                    self.token = self.getToken()
                    if (self.token.recognized_string == ")"):
                        self.token = self.getToken()
                        if (self.token.recognized_string == ":"):
                            self.token = self.getToken()
                            if (self.token.recognized_string == "#{"):
                                self.token = self.getToken()
                                self.declarations()
                                while (self.def_function()):
                                    pass
                                else:
                                    returns = False
                                self.statements()
                                if (self.token.recognized_string == "#}"):
                                    self.token = self.getToken()
                                else:
                                    self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                            else:
                                self.error("#{ expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                        else:
                            self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                    else:
                        self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            returns = False
        return returns
    
    def def_function(self):
        returns = True
        if (self.token.recognized_string == "def"):
            self.token = self.getToken()
            if (self.token.family == "idk"):
                self.token = self.getToken()
                if (self.token.recognized_string == "("):
                    self.token = self.getToken()
                    self.id_list()
                    if (self.token.recognized_string == ")"):
                        self.token = self.getToken()
                        if (self.token.recognized_string == ":"):
                            self.token = self.getToken()
                            if (self.token.recognized_string == "#{"):
                                self.token = self.getToken()
                                self.declarations()
                                while (self.def_function()):
                                    pass
                                else:
                                    returns = False
                                self.statements()
                                if (self.token.recognized_string == "#}"):
                                    self.token = self.getToken()
                                else:
                                    self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                            else:
                                self.error("#{ expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                        else:
                            self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                    else:
                        self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            returns = False
        return returns
    
    def declarations(self):
        while (self.token.recognized_string == "#declare"):
            self.declaration_line()
    
    def declaration_line(self):
        if (self.token.recognized_string == "#declare"):
            self.token = self.getToken()
            self.id_list()
        else:
            self.error("'#declare' expected, got " + self.token.recognized_string + " instead", self.token.line_number)
    
    def statement(self):
        if (self.token.recognized_string in ["while", "if"]):
            self.structured_statement()
        else:
            self.simple_statement()
    
    def statements(self):
        while (self.token.recognized_string in ["return", "print", "while", "if"] or self.token.family == "idk"):
            self.statement()

    def simple_statement(self):
        if (self.token.recognized_string == "print"):
            self.print_stat()
        elif (self.token.recognized_string == "return"):
            self.return_stat()
        else:
            self.assignment_stat()
    
    def structured_statement(self):
        if (self.token.recognized_string == "if"):
            self.if_stat()
        else:
            self.while_stat()
    
    def assignment_stat(self):
        if (self.token.family == "idk"):
            self.token = self.getToken()
            if (self.token.recognized_string == "="):
                self.token = self.getToken()
                if (self.token.recognized_string == "int"):
                    self.token = self.getToken()
                    if (self.token.recognized_string == "("):
                        self.token = self.getToken()
                        if (self.token.recognized_string == "input"):
                            self.token = self.getToken()
                            if (self.token.recognized_string == "("):
                                self.token = self.getToken()
                                if (self.token.recognized_string == ")"):
                                    self.token = self.getToken()
                                    if (self.token.recognized_string == ")"):
                                        self.token = self.getToken()
                                        if (self.token.recognized_string == ";"):
                                            self.token = self.getToken()
                                        else:
                                            self.error("; expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                                    else:
                                        self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                                else:
                                    self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                            else:
                                self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                        else:
                            self.error("'input' expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                    else:
                        self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.expression()
                    if (self.token.recognized_string == ';'):
                        self.token = self.getToken()
                    else:
                        self.error("; expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("= expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)

    def print_stat(self):
        if (self.token.recognized_string == "print"):
            self.token = self.getToken()
            if (self.token.recognized_string == "("):
                self.token = self.getToken()
                self.expression()
                if (self.token.recognized_string == ")"):
                    self.token = self.getToken()
                    if (self.token.recognized_string == ";"):
                        self.token = self.getToken()
                    else:
                        self.error("; expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("print expected, got " + self.token.recognized_string + " instead", self.token.line_number)                

    def return_stat(self):
        if (self.token.recognized_string == "return"):
            self.token = self.getToken()
            if (self.token.recognized_string == "("):
                self.token = self.getToken()
                self.expression()
                if (self.token.recognized_string == ")"):
                    self.token = self.getToken()
                    if (self.token.recognized_string == ";"):
                        self.token = self.getToken()
                    else:
                        self.error("; expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("return expected, got " + self.token.recognized_string + " instead", self.token.line_number)                
    
    def if_stat(self):
        if (self.token.recognized_string == "if"):
            self.token = self.getToken()
            if (self.token.recognized_string == "("):
                self.token = self.getToken()
                self.condition()
                if (self.token.recognized_string == ")"):
                    self.token = self.getToken()
                    if (self.token.recognized_string == ":"):
                        self.token = self.getToken()
                        if (self.token.recognized_string == "#{"):
                            self.token = self.getToken()
                            self.statements()
                            if (self.token.recognized_string == "#}"):
                                self.token = self.getToken()
                                if (self.token.recognized_string == "else"):
                                    self.token = self.getToken()
                                    if (self.token.recognized_string == ":"):
                                        self.token = self.getToken()
                                        if (self.token.recognized_string == "#{"):
                                            self.token = self.getToken()
                                            self.statements()
                                            if (self.token.recognized_string == "#}"):
                                                self.token = self.getToken()
                                            else:
                                                self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                                        else:
                                            self.statement()
                                    else:
                                        self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                            else:
                                self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                        else:
                            self.statement()
                            if (self.token.recognized_string == "else"):
                                self.token = self.getToken()
                                if (self.token.recognized_string == ":"):
                                    self.token = self.getToken()
                                    if (self.token.recognized_string == "#{"):
                                        self.token = self.getToken()
                                        self.statements()
                                        if (self.token.recognized_string == "#}"):
                                            self.token = self.getToken()
                                        else:
                                            self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                                    else:
                                        self.statement()
                                else:
                                    self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                    else:
                        self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("if expected, got " + self.token.recognized_string + " instead", self.token.line_number)
    
    def while_stat(self):
        if (self.token.recognized_string == "while"):
            self.token = self.getToken()
            if (self.token.recognized_string == "("):
                self.token = self.getToken()
                self.condition()
                if (self.token.recognized_string == ")"):
                    self.token = self.getToken()
                    if (self.token.recognized_string == ":"):
                        self.token = self.getToken()
                        if (self.token.recognized_string == "#{"):
                            self.token = self.getToken()
                            self.statements()
                            if (self.token.recognized_string == "#}"):
                                self.token = self.getToken()
                            else:
                                self.error("#} expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                        else:
                            self.statement()
                    else:
                        self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("( expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("while expected, got " + self.token.recognized_string + " instead", self.token.line_number)
    
    def id_list(self):
        if (self.token.family == "idk"):
            self.token = self.getToken()
            while (self.token.recognized_string == ","):
                self.token = self.getToken()
                if (self.token.family == "idk"):
                    self.token = self.getToken()
                else:
                    self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)
    
    def expression(self):
        self.optional_sign()
        self.term()
        while (self.token.family == "addOperator"):
            self.token = self.getToken()
            self.term()
    
    def term(self):
        self.factor()
        while (self.token.family == "mulOperator"):
            self.token = self.getToken()
            self.factor()
    
    def factor(self):
        if (self.token.family == 'number'):
            self.token = self.getToken()
        elif (self.token.recognized_string == '('):
            self.token = self.getToken()
            self.expression()
            if (self.token.recognized_string == ')'):
                self.token = self.getToken()
            else:
                self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        elif (self.token.family == 'idk'):
            self.token = self.getToken()
            self.idtail()
        else:
            self.error("Integer, expression or identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)

    def idtail(self):
        if (self.token.recognized_string == '('):
            self.token = self.getToken()
            self.actual_par_list()
            if (self.token.recognized_string == ')'):
                self.token = self.getToken()
            else:
                self.error(") expected, got " + self.token.recognized_string + " instead", self.token.line_number)

    def actual_par_list(self):
        self.expression()
        while (self.token.recognized_string == ','):
            self.token = self.getToken()
            self.expression()
    
    def optional_sign(self):
        if (self.token.family == "addOperator"):
            self.token = self.getToken()

    
    def condition(self):
        self.bool_factor()
        while (self.token.recognized_string == 'or'):
            self.token = self.getToken()
            self.bool_factor
    
    def bool_term(self):
        self.token = self.getToken()
        self.bool_factor()
        while (self.token.recognized_string == 'and'):
            self.token = self.getToken()
            self.bool_factor
    
    def bool_factor(self):
        if (self.token.recognized_string == "not"):
            self.token = self.getToken()
            if (self.token.recognized_string == '['):
                self.token = self.getToken()
                self.condition()
                if (self.token.recognized_string == ']'):
                    self.token = self.getToken()
                else:
                    self.error("[ expected, got" + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("] expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        elif (self.token.recognized_string == '['):
            self.token = self.getToken()
            self.condition()
            if (self.token.recognized_string == ']'):
                self.token = self.getToken()
            else:
                self.error("] expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.expression()
            if (self.token.family == 'relOperator'):
                self.token = self.getToken()
                self.expression()
            else:
                self.error("relational operator expected, got " + self.token.recognized_string + " instead", self.token.line_number)
    
    def call_main_part(self):
        if (self.token.recognized_string == "if"):
            self.token = self.getToken()
            if (self.token.recognized_string == '__name__'):
                self.token = self.getToken()
                if (self.token.recognized_string == '=='):
                    self.token = self.getToken()
                    if (self.token.recognized_string in ['\"__main__\"', "\'__main__\'"]):
                        self.token = self.getToken()
                        if (self.token.recognized_string == ':'):
                            self.token = self.getToken()
                            while (self.token.recognized_string != ''):
                                self.main_function_call()
                        else:
                            self.error(": expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                    else:
                        self.error("__main__ expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error("== expected, got " + self.token.recognized_string + " instead", self.token.line_number)
            else:
                self.error("__name__ expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("if expected, got " + self.token.recognized_string + " instead", self.token.line_number)

    
    def main_function_call(self):
        if (self.token.family == "idk"):
            self.token = self.getToken()
            if (self.token.recognized_string == '('):
                self.token = self.getToken()
                if (self.token.recognized_string == ')'):
                    self.token = self.getToken()
                    if(self.token.recognized_string == ';'):
                        self.token = self.getToken()
                    else:
                        self.error("Semicolon expected, got " + self.token.recognized_string + " instead", self.token.line_number)
                else:
                    self.error("Parenthesis not closed", self.token.line_number)
            else:
                self.error("Parenthesis expected, got " + self.token.recognized_string + " instead", self.token.line_number)
        else:
            self.error("Identifier expected, got " + self.token.recognized_string + " instead", self.token.line_number)

parser = Parser()
parser.syntax_analyzer()