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

# WILL BE EXECUTED - TEST THE LEX

out = open("lex.out", 'w')
out.write(testLex())
out.close()

#

#####  SYNTAX  #####

class Parser:

    def __init__(self):
        self.lexical_analyzer = Lex(sys.argv[1])
        self.tokens = []

    def syntax_analyzer(self):
        self.token = self.getToken()
        self.startRule()
        print("Compiled successfully")
    
    def getTokens(self):
        return self.tokens

    def getToken(self):
        self.tokens.append(self.lexical_analyzer.lex())
        return self.tokens[-1]
    
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

# WILL BE EXECUTED - TEST THE SYNTAXER

parser = Parser()
parser.syntax_analyzer()

#

##### INTERMEDIATE CODE #####
class Node:
    def __init__(self):
        self.name = None
        self.place = None
        self.true = None
        self.false = None

class Quad:
    tokenCounter = -1
    labelCounter = -1
    tempCounter = -1
    quads = []
    functionStack = []
    tokens=[]

    def __init__(self, label, operator, operand1, operand2, operand3):
        self.labelCounter = label
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.operand3 = operand3

    @staticmethod
    def genQuad(operator, operand1, operand2, operand3):
        Quad.labelCounter += 1
        Quad.quads.append(Quad(str(Quad.labelCounter), str(operator), str(operand1), str(operand2), str(operand3)))
    
    @staticmethod
    def nextQuad():
        return Quad.labelCounter + 1
    
    @staticmethod
    def newTemp():
        Quad.tempCounter += 1
        return "T%" + str(Quad.tempCounter)
    
    @staticmethod
    def emptyList():
        return []
    
    @staticmethod
    def makeList(label):
        return [label]
    
    @staticmethod
    def mergeList(list1, list2):
        return list1 + list2
    
    @staticmethod
    def backpatch(list, label):
        for element in list:
            Quad.quads[element].operand3 = str(label)
        del list

    @staticmethod
    def current_token():
        return Quad.tokens[Quad.tokenCounter].recognized_string
    
    @staticmethod
    def peek_tokens_ahead(ahead):
        return Quad.tokens[Quad.tokenCounter + ahead].recognized_string
    
    @staticmethod
    def next_token():
        Quad.tokenCounter += 1
        return Quad.tokens[Quad.tokenCounter].recognized_string

    @staticmethod
    def E(E: Node):
        T1 = Node()
        T2 = Node()
        Quad.T(T1)
        while (Quad.current_token() in ["+", "-"]):
            add = Quad.current_token() == "+"
            Quad.next_token()
            Quad.T(T2)
            w = Quad.newTemp()
            if (add):
                Quad.genQuad("+", T1.place, T2.place, w)
            else:
                Quad.genQuad("-", T1.place, T2.place, w)
            T1.place = w
        E.place = T1.place

    @staticmethod
    def T(T: Node):
        F1 = Node()
        F2 = Node()
        Quad.F(F1)
        while (Quad.current_token() in ["*", "//"]):
            mul = Quad.current_token() == "*"
            Quad.next_token()
            Quad.F(F2)
            w = Quad.newTemp()
            if (mul):
                Quad.genQuad("*", F1.place, F2.place, w)
            else:
                Quad.genQuad("//", F1.place, F2.place, w)
            F1.place = w
        T.place = F1.place

    @staticmethod
    def F(F: Node):
        if (Quad.current_token() == '('):
            Quad.next_token()
            E1 = Node()
            Quad.E(E1)
            Quad.next_token()
            F.place = E1.place
        else:
            if (Quad.peek_tokens_ahead(1) == "("):
                func_name = Quad.current_token()
                Quad.next_token() # ID
                while (Quad.current_token() in [",", "("]): # id list 
                    Quad.next_token() # ( or ,
                    E = Node()
                    Quad.E(E)
                    Quad.genQuad("par", E.place, "cv", "_")
                ID = Quad.newTemp()
                Quad.genQuad("par", ID, "ret", "_")
                Quad.genQuad("call", func_name, "_", "_")
            else:
                ID = Quad.current_token()
            Quad.next_token()
            F.place = ID

    @staticmethod
    def B(B: Node):
        Q1 = Node()
        Q2 = Node()
        Quad.Q(Q1)
        B.true  = Q1.true
        B.false = Q1.false
        while (Quad.current_token() == "or"):
            Quad.next_token()
            Quad.Q(Q2)
            Quad.backpatch(B.false, Quad.nextQuad())
            B.true = Quad.mergeList(B.true, Q2.true)
            B.false  = Q2.false
    
    @staticmethod
    def Q(Q: Node):
        R1 = Node()
        R2 = Node()
        Quad.R(R1)
        Q.true  = R1.true
        Q.false = R1.false
        while (Quad.current_token() == "and"):
            Quad.next_token()
            Quad.R(R2)
            Quad.backpatch(Q.true, Quad.nextQuad())
            Q.false = Quad.mergeList(Q.false, R2.false)
            Q.true  = R2.true

    @staticmethod
    def R(R: Node):
        if (Quad.current_token() == 'not'): # reversed
            Quad.next_token()
            if (Quad.current_token() == '['):
                Quad.next_token()
                B = Node()
                Quad.B(B)
                R.true = B.false
                R.false = B.true
        elif (Quad.current_token() == '['):
            Quad.next_token()
            B = Node()
            Quad.B(B)
            R.true = B.true
            R.false = B.false
        else:
            E1 = Node()
            E2 = Node()
            Quad.next_token()
            R.true = Quad.makeList(Quad.nextQuad())
            E1 = Node()
            Quad.E(E1)
            relop = Quad.current_token()
            Quad.next_token()
            E2 = Node()
            Quad.E(E2)
            Quad.genQuad(relop, E1.place, E2.place, '_')
            R.false = Quad.makeList(Quad.nextQuad())
            Quad.genQuad('jump', '_', '_', '_')

    @staticmethod
    def input():
        Quad.genQuad("in", Quad.current_token(), "_", "_")

    @staticmethod
    def print():
        Quad.next_token() # print
        Quad.next_token() # (
        E = Node()
        Quad.E(E)
        Quad.genQuad("out", E.place, "_", "_")

    @staticmethod
    def return_func():
        Quad.next_token() # return
        Quad.next_token() # (
        node = Node()
        Quad.E(node)
        Quad.genQuad("ret", "_", "_", node.place)
            

    @staticmethod
    def statement():
        if (Quad.current_token() == "if"):
            Quad.if_else()
        elif (Quad.current_token() == "while"):
            Quad.while_loop()
        elif (Quad.current_token() == "return"):
            Quad.return_func() 
            while (Quad.current_token() != ";"):
                Quad.next_token() # until ;
            Quad.next_token()
        elif (Quad.current_token() == "print"):
            Quad.print()
            Quad.next_token() # )
            Quad.next_token() # ;
        elif (Quad.peek_tokens_ahead(2) == "int"):
            Quad.input() # input
            while (Quad.current_token() != ";"):
                Quad.next_token() # id = int(input())
            Quad.next_token() # ;
        elif (Quad.peek_tokens_ahead(1) == "="):
            id = Quad.current_token()
            if (Quad.peek_tokens_ahead(3) == "("): # function call
                Quad.next_token() # ID
                Quad.next_token() # =
                func_name = Quad.current_token()
                Quad.next_token() # ID
                while (Quad.current_token() in [",","("]): # id list
                    Quad.next_token() # ( or ,
                    E = Node()
                    Quad.E(E)
                    Quad.genQuad("par", E.place, "cv", "_")
                Quad.genQuad("par", Quad.newTemp(), "ret", "_")
                Quad.genQuad("call", func_name, "_", "_")
                Quad.next_token() # )
                Quad.next_token() # ;
                Quad.genQuad("=", id, "_", "ret") # TODO - ?????
            else: # expression assign
                node = Node()
                Quad.next_token() # id
                Quad.next_token() # =
                Quad.E(node)
                Quad.genQuad("=", id, "_", node.place)
                Quad.next_token()

    @staticmethod
    def statements():
        while (Quad.current_token() != "#}"):
            Quad.statement()
        Quad.next_token()

    @staticmethod
    def declaration():
        Quad.next_token()
        Quad.next_token()
        if (Quad.current_token() == ","):
            Quad.next_token()
            Quad.next_token()

    @staticmethod
    def while_loop():
        condQuad = Quad.nextQuad()
        Quad.next_token() # while
        condition = Node()
        Quad.R(condition) # condition
        Quad.next_token() # )
        Quad.next_token() # :
        Quad.backpatch(condition.true, Quad.nextQuad())
        if (Quad.current_token() == "#{"):
            Quad.next_token()
            Quad.statements()
        else:
            Quad.statement()
        Quad.genQuad("jump", "_", "_", condQuad)
        Quad.backpatch(condition.false, Quad.nextQuad())

    @staticmethod
    def if_else():
        Quad.next_token() # if
        condition = Node()
        Quad.R(condition) # condition
        Quad.next_token() # )
        Quad.next_token() # :
        Quad.backpatch(condition.true, Quad.nextQuad())
        if (Quad.current_token() == "#{"):
            Quad.next_token()
            Quad.statements()
        else:
            Quad.statement()
        ifList = Quad.makeList(Quad.nextQuad())
        Quad.genQuad("jump", "_", "_", "_")
        Quad.backpatch(condition.false, Quad.nextQuad())
        if (Quad.current_token() == "else"):
            Quad.next_token()    # else
            Quad.next_token()    # :
            if (Quad.current_token() == "#{"):
                Quad.next_token()
                Quad.statements()
            else:
                Quad.statement()
            Quad.backpatch(ifList, Quad.nextQuad())
            

    @staticmethod
    def def_function():
        Quad.functionStack.append(Quad.current_token()) # ID
        Quad.next_token() # ID
        Quad.next_token() # (
        while (Quad.current_token() != ")"): # id list 
            Quad.next_token()
        Quad.next_token() # )
        Quad.next_token() # :
        Quad.next_token() # #{
        while (Quad.current_token() == "#declare"):
            Quad.declaration()
        while (Quad.current_token() == "def"):
            Quad.next_token() # def
            Quad.def_function()
        Quad.genQuad("begin_block", Quad.functionStack[-1], "_", "_")
        Quad.statements() # no need to check for #} afterwards. While loop ends on it
        Quad.genQuad("end_block", Quad.functionStack.pop(-1), "_", "_")
        
    @staticmethod
    def main_pilot():
        Quad.next_token()
        while (Quad.current_token() == "def"):
            Quad.next_token() # def
            Quad.def_function()
        while (Quad.current_token() != ":"):
            Quad.next_token() # if __name__ == "__main__"
        Quad.next_token()
        if (Quad.peek_tokens_ahead(-2) != "\"__main__\""):
            print("Error: program not named \"__main__\" !!!")
            exit(-1)
        Quad.genQuad("begin_block", "main", "_", "_")
        while (True):
            func_name = Quad.current_token()
            Quad.genQuad("call", func_name, "_", "_")
            Quad.next_token() # ID
            Quad.next_token() # (
            Quad.next_token() # )
            Quad.next_token() # ;
            if (Quad.tokenCounter >= len(Quad.tokens) - 1):
                break
        Quad.genQuad("halt", "_", "_", "_")
        Quad.genQuad("end_block", "main", "_", "_")

    @staticmethod
    def toString():
        string = 'label\toperator\t   op1\t\t\t\t\top2\t\top3\n'
        for quad in Quad.quads:
            string = string + quad.labelCounter + "\t\t"  + quad.operator + ' '*(15-len(quad.operator)) + quad.operand1 + ' '*(21-len(quad.operand1)) + quad.operand2 + ' '*(8-len(quad.operand2)) + quad.operand3 + "\n"
        return string

    @staticmethod
    def write_quads():
        file = open(sys.argv[1][:-3] + "int", 'w')
        file.write(Quad.toString())
        file.close

    @staticmethod
    def intermediate():
        parser = Parser()
        parser.syntax_analyzer()
        Quad.tokens = parser.getTokens()
        Quad.main_pilot()
        Quad.write_quads()

###### TEST INTERMEDIATE ######
Quad.intermediate()
        