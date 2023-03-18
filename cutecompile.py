import sys

# STATES          FINAL STATES        ERRORS
S_START = 0   ;   F_NUM   = 100   ;   E_SLC   = -1
S_DIG   = 1   ;   F_IDK   = 101   ;   E_NAV   = -2
S_IDK   = 2   ;   F_GROUP = 102   ;   E_ILGBR = -3
S_HASH  = 3   ;   F_DELIM = 103   ;   E_BDHSH = -4
S_REM   = 4   ;   F_ASGN  = 104   ;   E_ILDOL = -5
S_EOC   = 5   ;   F_RELOP = 105   ;   
S_LST   = 6   ;   F_ADDOP = 106   ;   
S_GRT   = 7   ;   F_MULOP = 107   ;  
S_EQUAL = 8
S_DIFF  = 9

#                    empty  , chr/_  , nums  ,  +/-    , *//    , <      , >      , !      , =      , sep    , ()/[]  , {}     , #      , $  
stateautomation = {{ S_START, S_IDK  , S_DIG ,  F_ADDOP, F_MULOP, S_LST  , S_GRT  , S_DIFF , S_EQUAL, F_DELIM, F_GROUP, E_ILGBR, S_HASH , E_ILDOL }, # 0 - Start
                   { F_NUM  , E_NAV  , S_DIG ,  F_NUM  , F_NUM  , F_NUM  , F_NUM  , F_NUM  , F_NUM  , F_NUM  , F_NUM  , E_ILGBR, F_NUM  , F_NUM   }, # 1 - Dig
                   { S_IDK  , S_IDK  , S_IDK ,  F_IDK  , F_IDK  , F_IDK  , F_IDK  , F_IDK  , F_IDK  , F_IDK  , F_IDK  , E_ILGBR, F_IDK  , F_IDK   }, # 2 - Idk
                   { E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, E_BDHSH, S_REM   }, # 3 - Hashtag
                   { S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_EOC   }, # 4 - Remove
                   { S_EOC  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_REM  , S_START }, # 5 - Exit Comment
                   { F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, S_LST  , F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP }, # 6 - Smaller than
                   { F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP, S_GRT  , F_RELOP, F_RELOP, F_RELOP, F_RELOP, F_RELOP }, # 7 - Larger than
                   { F_ASGN , F_ASGN , F_ASGN , F_ASGN , F_ASGN , F_ASGN , F_ASGN , F_ASGN , S_EQUAL, F_ASGN , F_ASGN , F_ASGN , F_ASGN , F_ASGN  }, # 8 - Equals
                   { E_SLC  , E_SLC  , E_SLC  , E_SLC  , E_SLC  , E_SLC  , E_SLC  , E_SLC  , F_RELOP, E_SLC  , E_SLC  , E_SLC  , E_SLC  , E_SLC   }  # 9 - Diff
                  }

stack = ' ' # this is the last character read

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
    
    def lex(file):
        stack = ' '
        string = ''
        # while ?
        char = file.read(1)
        # Remember to increment currentline 
        # every time \n is met
        return Token(string, 'dig', lex.currentLine)
    

file = open(sys.argv[1], 'r')
# Create lex object
lex = Lex(0)
# Return next token
lex.token = lex.lex(file)
file.close