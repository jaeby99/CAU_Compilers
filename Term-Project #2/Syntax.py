import sys

#define SLR_table
SLR_table = {'0':{'vtype' : 's4', '$' : 'r3', 'CODE' : '1', 'VDECL' : '3', 'FDECL' : '2'},
             '1':{'$' : "accept"},
             '2':{'vtype' : 's4', '$' : 'r3', 'CODE' : '5'},
             '3':{'vtype' : 's4', '$' : 'r3', 'CODE' : '6', 'VDECL' : '3', 'FDECL' : '2'},
             '4':{'id' : 's7'},
             '5':{'$' : 'r1'},
             '6':{'$' : 'r2'},
             '7':{'semi' : 's9', 'lparen' : 's8'},
             '8':{'vtype' : 's11', 'rparen' : 'r9', 'ARG': '10'},
             '9':{'vtype' : 'r4', 'id' : 'r4', 'rbrace' :'r4', 'if' : 'r4', 'while' : 'r4', 'return' : 'r4', '$' : 'r4'},
             '10':{'rparen' : 's12'},
             '11':{'id': 's13'},
             '12':{'lbrace' : 's14'},
             '13':{'rparen' : 'r8', 'comma' :'s16', 'MOREARGS': '15'},
             '14':{'vtype': 's23', 'id': 's20', 'rbrace': 'r11', 'if':'s21', 'while': 's22', 'return': 'r11', 'VDECL': '19', 'BLOCK': '17', 'STMT': '18'},
             '15':{'rparen': 'r6'},
             '16':{'vtype': 's24'},
             '17':{'return': 's26', 'RETURN': '25'},
             '18':{'vtype': 's23', 'id': 's20', 'rbrace': 'r11', 'if': 's21', 'while': 's22', 'return': 'r11', 'VDECL': '19', 'BLOCK': '27', 'STMT': '18'},
             '19':{'vtype': 'r12', 'id': 'r12', 'rbrace': 'r12', 'if': 'r12', 'while': 'r12', 'return': 'r12'},
             '20':{'assign': 's28'},
             '21':{'lparen': 's29'},
             '22':{'lparen': 's30'},
             '23':{'id': 's31'},
             '24':{'id': 's32'},
             '25':{'rbrace': 's33'},
             '26':{'id': 's36', 'lparen': 's35', 'num': 's37', 'FACTOR': '34'},
             '27':{'rbrace': 'r10', 'return': 'r10'},
             '28':{'id': 's36', 'lparen': 's35', 'literal': 's40', 'num': 's37', 'RHS': '38', 'EXPR': '39', 'TERM': '41', 'FACTOR': '42'},
             '29':{'id': 's36', 'lparen': 's35', 'num': 's37', 'FACTOR': '44', 'COND': '43'},
             '30':{'id': 's36', 'lparen': 's35', 'num': 's37', 'FACTOR': '44', 'COND': '45'},
             '31':{'semi': 's9'},
             '32':{'rparen': 'r8', 'comma': 's16', 'MOREARGS': '46'},
             '33':{'vtype': 'r5', '$': 'r5'},
             '34':{'semi': 's47'},
             '35':{'id': 's36', 'lparen': 's35', 'num': 's37', 'EXPR': '48', 'TERM': '41', 'FACTOR': '42'},
             '36':{'semi': 'r23', 'rparen': 'r23', 'addsub': 'r23', 'multdiv': 'r23', 'comp': 'r23'},
             '37':{'semi': 'r24', 'rparen': 'r24', 'addsub': 'r24', 'multdiv': 'r24', 'comp': 'r24'},
             '38':{'semi': 's49'},
             '39':{'semi': 'r16'},
             '40':{'semi': 'r17'},
             '41':{'semi': 'r19', 'rparen': 'r19', 'addsub': 's50'},
             '42':{'semi': 'r21', 'rparen': 'r21', 'addsub': 'r21', 'multdiv': 's51'},
             '43':{'rparen': 's52'},
             '44':{'comp': 's53'},
             '45':{'rparen': 's54'},
             '46':{'rparen': 'r7'},
             '47':{'rbrace': 'r26'},
             '48':{'rparen': 's55'},
             '49':{'vtype': 'r13', 'id': 'r13', 'rbrace': 'r13', 'if': 'r13', 'while': 'r13', 'return': 'r13'},
             '50':{'id': 's36', 'lparen': 's35', 'num': 's37', 'EXPR': '56', 'TERM': '41', 'FACTOR': '42'},
             '51':{'id': 's36', 'lparen': 's35', 'num': 's37', 'TERM': '57', 'FACTOR': '42'},
             '52':{'lbrace': 's58'},
             '53':{'id': 's36', 'lparen': 's35', 'num': 's37', 'FACTOR': '59'},
             '54':{'lbrace': 's60'},
             '55':{'semi': 'r22', 'rparen': 'r22', 'addsub': 'r22', 'multdiv': 'r22', 'comp': 'r22'},
             '56':{'semi': 'r18', 'rparen': 'r18'},
             '57':{'semi': 'r20', 'rparen': 'r20', 'addsub': 'r20'},
             '58':{'vtype':'s23', 'id': 's20', 'rbrace': 'r11', 'if': 's21', 'while': 's22', 'return': 'r11', 'VDECL': '19', 'BLOCK': '61', 'STMT': '18'},
             '59':{'rparen': 'r25'},
             '60':{'vtype':'s23', 'id': 's20', 'rbrace': 'r11', 'if': 's21', 'while': 's22', 'return': 'r11', 'VDECL': '19', 'BLOCK': '62', 'STMT': '18'},
             '61':{'rbrace': 's63'},
             '62':{'rbrace': 's64'},
             '63':{'else': 's65'},
             '64':{'vtype': 'r15', 'id':'r15', 'rbrace': 'r15', 'if': 'r15', 'while': 'r15', 'return': 'r15'},
             '65':{'lbrace': 's66'},
             '66':{'vtype':'s23', 'id': 's20', 'rbrace': 'r11', 'if': 's21', 'while': 's22', 'return': 'r11', 'VDECL': '19', 'BLOCK': '67', 'STMT': '18'},
             '67':{'rbrace': 's68'},
             '68':{'vtype':'r14', 'id': 'r14', 'rbrace': 'r14', 'if': 'r14', 'while': 'r15', 'return': 'r14'}
             }

#define result of production
Production = {'r0' : 'CODE-', 'r1' : 'CODE', 'r2' : 'CODE', 'r3' : 'CODE', 'r4' : 'VDECL', 'r5' : 'FDECL', 'r6' : 'ARG', 'r7' : 'MOREARGS', 'r8' : 'MOREARGS', 'r9' : 'ARG',
              'r10' : 'BLOCK', 'r11' : 'BLOCK', 'r12' : 'STMT', 'r13' : 'STMT', 'r14' : 'STMT', 'r15' : 'STMT', 'r16' : 'RHS',
              'r17' : 'RHS', 'r18' : 'EXPR', 'r19' : 'EXPR', 'r20' : 'TERM', 'r21' : 'TERM', 'r22' : 'FACTOR', 'r23' : 'FACTOR', 'r24' : 'FACTOR', 'r25' : 'COND', 'r26' : 'RETURN'}

#define tokens used in production
Reduced_word = {'r0': 1, 'r1' : 2, 'r2' : 2, 'r3' : 0, 'r4' : 3, 'r5' : 9, 'r6' : 3, 'r7' : 4, 'r8' : 0, 'r9' : 0,
              'r10' : 2, 'r11' : 0, 'r12' : 1, 'r13' : 4, 'r14' : 11, 'r15' : 7, 'r16' : 1,
              'r17' : 1, 'r18' : 3, 'r19' : 1, 'r20' : 3, 'r21' : 1, 'r22' : 3, 'r23' : 1, 'r24' : 1, 'r25' : 3, 'r26' : 3}

#For the ouput message
def ith_character(i):
    if i==1:
        return "1st"
    elif i==2:
        return "2nd"
    else:
        return str(i) + "th"

#define syntax error
def Syntax_error(char, state):
    if char in SLR_table[state].keys():
        return True
    else:
        return False

#Syntax analyzer
def Syntax_Analyzer(Token, file):
    state_stack = []
    state = '0'
    state_stack.append(state)
    a = ' '
    i = 0
    while a != "accept":
        #end of token(epsilon)
        if i == len(Token):
            char = '$'
        #shift words
        if a[0] != 'r' and i != len(Token):
            char = Token[i]

        #Find action from SLR table
        if Syntax_error(char, state):
            a = SLR_table[state][char]
        #Error
        else:
            file.write("\nSyntax error at " + ith_character(i+1) +" token "+": " + str(SLR_table[state].keys()) + " are expected but '" + str(char) + "' came")
            sys.exit()

        #shift action
        if a[0] == 's':
            state = a[1:]
            state_stack.append(state)
            i += 1
        #reduce action
        elif a[0] == 'r':
            rw = Production[a]
            # Reduce 액션으로 stack에서 이전 state들 pop
            for j in range(Reduced_word[a]):
                state_stack.pop()

            # GOTO from SLR table
            if Syntax_error(rw, state_stack[-1]):
                state = SLR_table[state_stack[-1]][rw]
            #Error
            else:
                file.write("\nSyntax error at " + ith_character(i + 1) + " token " + ": " + str(SLR_table[state].keys()) + " are expected but '" + str(char) + "' came")
                sys.exit()
            # New State from GOTO
            state_stack.append(state)

    #success
    if a == "accept":
        file.write("\n    Input file has no Lexical && Syntax Error    ")
