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
S_DIFF  = 9
S_DIV   = 10

# state automation   empty   ,  char/_  ,  nums    ,  + or -  ,  *       ,  /       ,  <       ,  >       ,  !       ,  =       ,  :/,/;   ,  () or [],  {}      ,  #       ,  $       ,  EOF
stateAutomation = [[ S_START ,  S_IDK   ,  S_DIG   ,  F_ADDOP ,  F_MULOP ,  S_DIV   ,  S_LST   ,  S_GRT   ,  S_DIFF  ,  S_EQUAL ,  F_DELIM ,  F_GROUP ,  E_ILGBR ,  S_HASH  ,  E_ILDOL ,  F_EOF   ], # 0  -  Start
                   [ F_NUM   ,  E_NAV   ,  S_DIG   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  E_ILGBR ,  F_NUM   ,  F_NUM   ,  F_NUM   ], # 1  -  Dig
                   [ F_IDK   ,  S_IDK   ,  S_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  E_ILGBR ,  F_IDK   ,  F_IDK   ,  F_IDK   ], # 2  -  Idk
                   [ E_BDHSH ,  S_IDK   ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  F_GROUP ,  E_BDHSH ,  S_REM   ,  E_BDHSH ], # 3  -  Hashtag
                   [ S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_EOC   ,  E_EOF   ], # 4  -  Remove
                   [ S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_START ,  S_EOC   ,  E_EOF   ], # 5  -  Exit Comment
                   [ F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_LST   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ], # 6  -  Smaller than
                   [ F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_GRT   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ], # 7  -  Larger than
                   [ F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  E_BDASN ,  S_EQUAL ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ], # 8  -  Equals
                   [ E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  F_RELOP ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ], # 9  -  Different than
                   [ E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  F_MULOP ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ]  # 10 -  Divide
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
          "Bad assign"
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
        self.currentLine = 0
        self.token = None
        self.buffer = ' ' # this can be used to pass the last character read
                          # from the previous token to the next, in case it's needed

    # associates character to it's respective identifier code
    def charcode(self, char):
        if   (char == ' ' or char == '\n' or char == '\t'): # whitespace
            return 0
        elif (char >= 'A' and char <= 'z' and char not in ['[','/',']','^','`']): # a to Z and _
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
            print("ERROR: " + errors[state*(-1)] + " at line " + str(self.currentLine) + " !!")
            return Token(string, "error", self.currentLine)
        
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

    print("recognized string  |  family  |  line number")
    for i in range(0, len(tokens)):
        tk = tokens[i]
        print("\'" + tk.recognized_string + "\'  |  " + tk.family + "  |  " + str(tk.line_number))

    
testLex()


#####  SYNTAX  #####

class Parser:
# properties : recognized \ _string , family , line_number
    def __init__(self):
        self.lexical_analyzer = Lex(sys.argv[1])

    def syntax_analyzer(self):
        global token
        token = self.getToken()
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
        global token
        token = self.getToken()
        self.def_main_function(token)
        while (token.recognized_string == 'def'):
            self.def_main_function()
    
    def def_main_function(self, tokenin):
        returns = True
        global token
        token = tokenin
        if (token.recognized_string == "def"):
            token = self.getToken()
            if (token.family == "idk"):
                token = self.getToken()
                if (token.recognized_string == "("):
                    token = self.getToken()
                    if (token.recognized_string == ")"):
                        token = self.getToken()
                        if (token.recognized_string == ":"):
                            token = self.getToken()
                            if (token.recognized_string == "#{"):
                                token = self.getToken()
                                self.declarations()
                                while (self.def_function()):
                                    pass
                                else:
                                    returns = False
                                self.statements()
                                if (token.recognized_string == "#}"):
                                    token = self.getToken()
                                else:
                                    self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                            else:
                                self.error("#{ expected, got " + token.recognized_string + " instead", token.line_number)
                        else:
                            self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                    else:
                        self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            returns = False
        return returns
    
    def def_function(self):
        returns = True
        global token
        token = self.getToken()
        if (token.recognized_string == "def"):
            token = self.getToken()
            if (token.family == "idk"):
                token = self.getToken()
                if (token.recognized_string == "("):
                    token = self.getToken()
                    self.id_list()
                    if (token.recognized_string == ")"):
                        token = self.getToken()
                        if (token.recognized_string == ":"):
                            token = self.getToken()
                            if (token.recognized_string == "#{"):
                                token = self.getToken()
                                self.declarations()
                                while (self.def_function()):
                                    pass
                                else:
                                    returns = False
                                self.statements()
                                if (token.recognized_string == "#}"):
                                    token = self.getToken()
                                else:
                                    self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                            else:
                                self.error("#{ expected, got " + token.recognized_string + " instead", token.line_number)
                        else:
                            self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                    else:
                        self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            returns = False
        return returns
    
    def declarations(self):
        global token
        token = self.getToken()
        while (token.recognized_string == "#declare"):
            self.declaration_line(token)
    
    def declaration_line(self, tokenin):
        global token
        token = tokenin
        if (token.recognized_string == "#declare"):
            token = self.getToken()
            self.id_list()
        else:
            self.error("'#declare' expected, got " + token.recognized_string + " instead", token.line_number)
    
    def statement(self, tokenin):
        if (tokenin.recognized_string in ["while", "if"]):
            self.structured_statement(tokenin)
        else:
            self.simple_statement(tokenin)
    
    def statements(self):
        global token
        token = self.getToken()
        while (token.recognized_string in ["return", "print", "while", "if"] or token.family == "idk"):
            self.statement(token)

    def simple_statement(self, tokenin):
        global token
        token = tokenin
        if (token.recognized_string == "print"):
            self.print_stat(token)
        elif (token.recognized_string == "return"):
            self.return_stat(token)
        else:
            self.assignment_stat(token)
    
    def structured_statement(self, tokenin):
        global token
        token = tokenin
        if (token == "if"):
            self.if_stat(token)
        else:
            self.while_stat(token)
    
    def assignment_stat(self, tokenin):
        global token
        token = tokenin
        if (token.family == "idk"):
            token = self.getToken()
            if (token.recognized_string == "="):
                token = self.getToken()
                if (token.recognized_string == "int"):
                    token = self.getToken()
                    if (token.recognized_string == "("):
                        token = self.getToken()
                        if (token.recognized_string == "input"):
                            token = self.getToken()
                            if (token.recognized_string == "("):
                                token = self.getToken()
                                if (token.recognized_string == ")"):
                                    token = self.getToken()
                                    if (token.recognized_string == ")"):
                                        token = self.getToken()
                                        if (token.recognized_string == ";"):
                                            token = self.getToken()
                                        else:
                                            self.error("; expected, got " + token.recognized_string + " instead", token.line_number)
                                    else:
                                        self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
                                else:
                                    self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
                            else:
                                self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
                        else:
                            token = self.getToken()
                            self.expression()
                            if (token.recognized_string == ';'):
                                token = self.getToken()
                            else:
                                self.error("; expected, got " + token.recognized_string + " instead", token.line_number)
                    else:
                        self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error("'int' expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("= expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)

    def print_stat(self, tokenin):
        global token
        token = tokenin
        if (token.recognized_string == "print"):
            token = self.getToken()
            if (token.recognized_string == "("):
                token = self.getToken()
                self.expression()
                if (token.recognized_string == ")"):
                    token = self.getToken()
                    if (token.recognized_string == ";"):
                        token = self.getToken()
                    else:
                        self.error("; expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("print expected, got " + token.recognized_string + " instead", token.line_number)                

    def return_stat(self, tokenin):
        global token
        token = tokenin
        if (token.recognized_string == "return"):
            token = self.getToken()
            if (token.recognized_string == "("):
                token = self.getToken()
                self.expression()
                if (token.recognized_string == ")"):
                    token = self.getToken()
                    if (token.recognized_string == ";"):
                        token = self.getToken()
                    else:
                        self.error("; expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("return expected, got " + token.recognized_string + " instead", token.line_number)                
    
    def if_stat(self, tokenin):
        global token
        token = tokenin
        if (token.recognized_string == "if"):
            token = self.getToken()
            if (token.recognized_string == "("):
                token = self.getToken()
                self.condition()
                if (token.recognized_string == ")"):
                    token = self.getToken()
                    if (token.recognized_string == ":"):
                        token = self.getToken()
                        if (token.recognized_string == "#{"):
                            token = self.getToken()
                            self.statements()
                            if (token.recognized_string == "#}"):
                                token = self.getToken()
                                if (token.recognized_string == "else"):
                                    token = self.getToken()
                                    if (token.recognized_string == ":"):
                                        token = self.getToken()
                                        if (token.recognized_string == "#{"):
                                            token = self.getToken()
                                            self.statements()
                                            if (token.recognized_string == "#}"):
                                                token = self.getToken()
                                            else:
                                                self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                                        else:
                                            self.statement()
                                    else:
                                        self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                            else:
                                self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                        else:
                            self.statement()
                            if (token.recognized_string == "else"):
                                token = self.getToken()
                                if (token.recognized_string == ":"):
                                    token = self.getToken()
                                    if (token.recognized_string == "#{"):
                                        token = self.getToken()
                                        self.statements()
                                        if (token.recognized_string == "#}"):
                                            token = self.getToken()
                                        else:
                                            self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                                    else:
                                        self.statement()
                                else:
                                    self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                    else:
                        self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("if expected, got " + token.recognized_string + " instead", token.line_number)
    
    def while_stat(self, tokenin):
        global token
        token = tokenin #self.getToken()
        if (token.recognized_string == "while"):
            token = self.getToken()
            if (token.recognized_string == "("):
                token = self.getToken()
                self.condition()
                if (token.recognized_string == ")"):
                    token = self.getToken()
                    if (token.recognized_string == ":"):
                        token = self.getToken()
                        if (token.recognized_string == "#{"):
                            token = self.getToken()
                            self.statements()
                            if (token.recognized_string == "#}"):
                                token = self.getToken()
                            else:
                                self.error("#} expected, got " + token.recognized_string + " instead", token.line_number)
                        else:
                            self.statement()
                    else:
                        self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("( expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("while expected, got " + token.recognized_string + " instead", token.line_number)
    
    def id_list(self):
        global token
        token = self.getToken()
        if (token.family == "idk"):
            token = self.getToken()
            while (token.recognized_string == ","):
                token = self.getToken()
                if (token.family == "idk"):
                    token = self.getToken()
                else:
                    self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)
    
    def expression(self):
        global token
        self.optional_sign()
        self.term()
        while (token.family == "addOperator"):
            token = self.getToken()
            self.term()
    
    def term(self):
        global token
        self.factor()
        while (token.family == "mulOperator"):
            self.getToken()
            self.factor()
    
    def factor(self):
        global token
        token = self.getToken()
        if (token.family == 'number'):
            token = self.getToken()
        elif (token.recognized_string == '('):
            token = self.getToken()
            self.expression()
            if (token.recognized_string == ')'):
                token = self.getToken()
            else:
                self.error(") expected, got " + token.recognized_string + " instead", token.line_number)
        elif (token.family == 'idk'):
            token = self.getToken()
            self.idtail()
        else:
            self.error("Integer, expression or identifier expected, got " + token.recognized_string + " instead", token.line_number)

    def idtail(self):
        global token
        token = self.getToken()
        if (token.recognized_string == '('):
            token = self.getToken()
            self.actual_par_list()
            if (token.recognized_string == ')'):
                token = self.getToken()
            else:
                self.error(") expected, got " + token.recognized_string + " instead", token.line_number)

    def actual_par_list(self):
        global token
        token = self.getToken()
        self.expression()
        while (token.recognized_string == ','):
            token = self.getToken()
            self.expression()
    
    def optional_sign(self):
        global token
        token = self.getToken()
        if (self.family == "addOperator"):
            token = self.getToken()

    
    def condition(self):
        global token
        token = self.getToken()
        self.bool_factor()
        while (token.recognized_string == 'or'):
            token = self.getToken()
            self.bool_factor
    
    def bool_term(self):
        global token
        token = self.getToken()
        self.bool_factor()
        while (token.recognized_string == 'and'):
            token = self.getToken()
            self.bool_factor
    
    def bool_factor(self):
        global token
        token = self.getToken()
        if (token.recognized_string == "not"):
            token = self.getToken()
            if (token.recognized_string == '['):
                token = self.getToken()
                self.condition()
                if (token.recognized_string == ']'):
                    token = self.getToken()
                else:
                    self.error("[ expected, got" + token.recognized_string + " instead", token.line_number)
            else:
                self.error("] expected, got " + token.recognized_string + " instead", token.line_number)
        elif (token.recognized_string == '['):
            token = self.getToken()
            self.condition()
            if (token.recognized_string == ']'):
                token = self.getToken()
            else:
                self.error("] expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.expression()
            if (token.family == 'relOperator'):
                self.getToken()
            else:
                self.error("relational operator expected, got " + token.recognized_string + " instead", token.line_number)
            self.expression()
    
    def call_main_part(self):
        global token
        token = self.getToken()
        if (token.recognized_string == "if"):
            token = self.getToken()
            if (token.recognized_string == '__name__'):
                token = self.getToken()
                if (token.recognized_string == '=='):
                    token = self.getToken()
                    if (token.recognized_string == '__main__'):
                        token = self.getToken()
                        if (token.recognized_string == ':'):
                            token = self.getToken()
                            if (token.recognized_string == 'def'):
                                token = self.getToken()
                                self.main_function_call()
                                while (token.recognized_string == 'def'):
                                    token = self.getToken()
                                    self.main_function_call()
                            else:
                                self.error("At least one define needed", token.line_number)
                        else:
                            self.error(": expected, got " + token.recognized_string + " instead", token.line_number)
                    else:
                        self.error("__main__ expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error("== expected, got " + token.recognized_string + " instead", token.line_number)
            else:
                self.error("__name__ expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("if expected, got " + token.recognized_string + " instead", token.line_number)

    
    def main_function_call(self):
        global token
        token = self.getToken()
        if (token.family == "idk"):
            token = self.getToken()
            if (token.recognized_string == '('):
                token = self.getToken()
                if (token.recognized_string == ')'):
                    token = self.getToken()
                    if(token.recognized_string == ';'):
                        token = self.getToken()
                    else:
                        self.error("Semicolon expected, got " + token.recognized_string + " instead", token.line_number)
                else:
                    self.error("Parenthesis not closed", token.line_number)
            else:
                self.error("Parenthesis expected, got " + token.recognized_string + " instead", token.line_number)
        else:
            self.error("Identifier expected, got " + token.recognized_string + " instead", token.line_number)

parser = Parser()
parser.syntax_analyzer()