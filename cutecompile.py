import sys

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
S_EQUAL = 8   ;   F_MULOP = 108
S_DIFF  = 9
S_DIV   = 10

# state automation   empty   ,  char/_  ,  nums    ,  + or -  ,  *       ,  /       ,  <       ,  >       ,  !       ,  =       ,  :/,/;   ,  () or [],  {}      ,  #       ,  $       ,  EOF
stateAutomation = {{ S_START ,  S_IDK   ,  S_DIG   ,  F_ADDOP ,  F_MULOP ,  S_DIV   ,  S_LST   ,  S_GRT   ,  S_DIFF  ,  S_EQUAL ,  F_DELIM ,  F_GROUP ,  E_ILGBR ,  S_HASH  ,  E_ILDOL ,  F_EOF}, # 0  -  Start
                   { F_NUM   ,  E_NAV   ,  S_DIG   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  F_NUM   ,  E_ILGBR ,  F_NUM   ,  F_NUM   ,  E_EOF}, # 1  -  Dig
                   { F_IDK   ,  S_IDK   ,  S_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  F_IDK   ,  E_ILGBR ,  F_IDK   ,  F_IDK   ,  E_EOF}, # 2  -  Idk
                   { E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  E_BDHSH ,  F_GROUP ,  E_BDHSH ,  S_REM   ,  E_EOF}, # 3  -  Hashtag
                   { S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_EOC   ,  E_EOF}, # 4  -  Remove
                   { S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_REM   ,  S_START ,  E_EOF}, # 5  -  Exit Comment
                   { F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_LST   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  E_EOF}, # 6  -  Smaller than
                   { F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  S_GRT   ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  F_RELOP ,  E_EOF}, # 7  -  Larger than
                   { F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  S_EQUAL ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  F_ASGN  ,  E_EOF}, # 8  -  Equals
                   { E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  F_RELOP ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_IEXCL ,  E_EOF}, # 9  -  Different than
                   { E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  F_MULOP ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_BDDIV ,  E_EOF}  # 10 -  Divide
                  }

# lectic unit strings
lecticUnits = {"",
               "number",
               "idk",
               "group",
               "delimiter",
               "assignment",
               "relOperator",
               "addOperator",
               "mulOperator"
               }

# error explanations
errors = {"Illegal EOF",
          "Illegal character",
          "Illegal !",
          "Variables cannot start with a number",
          "Illegal bracket",
          "Hashtags need to be followed by $ or brackets",
          "Illegal $",
          "/ can only be followed by another /"
          }

# this can be used to pass the last character read
# from the previous token to the next, in case it's needed
buffer = ''

# ERRORS
# -1  - solo char

class Token:
# properties : recognized \ _string , family , line_number
    def __init__(recognized_string , family , line_number):
        self.recognized_string = recognized_string
        self.family = family
        self.line_number = line_number

class Lex:
    def __init__(filename, currentLine, token):
        self.filename = filename
        self.currentLine = currentLine
        self.token = token
        self.charStack = ' '

    # associates character to it's respective identifier code
    def charcode(char):
        if   (char == ' ' | char == '\n' | char == '\t'): # whitespace
            return 0
        elif (char > 65 & char < 122 & char != '`'): # a to Z and _
            return 1
        elif (char > 48 & char < 57): # 0 to 9
            return 2
        elif (char == '+' & '-' ): # + or -
            return 3
        elif (char == '*' & '/' ): # * or /
            return 4
        elif (char == '<'): # <
            return 5
        elif (char == '>'): # >
            return 6
        elif (char == '!'): # !
            return 7
        elif (char == '='): # =
            return 8
        elif (char == ':' & ',' & ';'): # : or , or ;
            return 9
        elif (char == '(' & ')' & '[' & ']'): # ( or ) or [ or ]
            return 10
        elif (char == '{' & '}'): # { or }
            return 11
        elif (char == '#'): # #
            return 12
        elif (char == '$'): # $
            return 13
        elif (char == ''): # EOF
            return 14
        else:
            return -1

    
    def lex(file):
        string = ''
        state = S_START
        while (state >= 0 & state < 100):

            # if there's a character in the buffer, retrieve it and empty the buffer
            if (buffer == ''):
                char = file.read(1)
            else:
                char = buffer
                buffer = ''
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
            if (state != S_START & state != F_NUM & state != F_IDK & state != F_ASGN & state != F_RELOP):
                string += char
            else:
                buffer = char
            
            # count possible next lines
            if (char == '\n'):
                self.currentLine += 1
        
        # if code is an error, process it
        if (state < 0):
            print("ERROR: " + errors[state*(-1)] + " at line " + self.currentLine + " !!")
            return Token(string, "error", lex.currentLine)
        
        return Token(string, lecticUnits[state - 100], lex.currentLine)
    

# Open file
file = open(sys.argv[1], 'r')

# Create lex object
lex = Lex(0)

# Return next token
lex.token = lex.lex(file)

# Close file
file.close