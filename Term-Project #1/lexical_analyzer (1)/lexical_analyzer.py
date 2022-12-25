#define token class
keyword=['if', 'IF', 'else', 'ELSE', 'while', 'WHILE', 'return', 'RETURN']
type_int=['int', 'INT']
type_char=['char', 'CHAR']
type = type_int + type_char
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd','e', 'f','g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = uppercase + lowercase
single_operator=['=', '>', '<','!']
double_operator=['==','!=','>=','<=']
operator= single_operator + double_operator
arth_operator=['+', '-', '*', '/']
terminate=[';']
pair=[')' , '(' , '{', '}']
comma=[',']
white_space=['\n', '\t', ' ']
quote=['"']
excla=['!']

#각각의 state transition별로 dictionary에는 없으나 lexical analyzer에 허용된 문자들
#'!'는 '!='가 출력될 수도 있기에 넣어둠
allwords = keyword + type + operator + arth_operator + terminate + pair + comma + white_space + excla
allwordsID = allwords + quote+excla
allwordsNum = allwordsID + alphabet+excla
alloperator = arth_operator + terminate + pair + comma + single_operator

#define Integer, Literal_String, Identifier state transition
Int_dfa = { 0:{'0':3, '-':1, '1':2, '2':2, '3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2 },
            1:{'1':2, '2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2},
            2:{'0':2,'1':2, '2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2},
            3:{}}

Lit_dfa ={0:{'"':1},
          1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1
          ,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1,
          '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1, '\n':1, '\t':1, ' ':1, '"':2},
          2:{}}

Id_dfa ={0:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1
          ,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1},
         1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1
          ,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1,
            '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}}

#Lexeme을 읽고 state transition을 통한 최종 state값을 return
def transition(dfa, s):
    state=0
    for c in s:
        if c in dfa[state].keys():
            state=dfa[state][c]
        else:
            return -1
    return state

def print_word(lexeme):
    if lex in type_int:
        fileoutput.write("      <VTYPE, INT>      \n")
    elif lex in type_char:
        fileoutput.write("      <VTYPE, CHAR>      \n")
    elif lex=='if' or lex=='IF':
        fileoutput.write("      <IF>      \n")
    elif lex=='else' or lex=='ELSE':
        fileoutput.write("      <ELSE>      \n")
    elif lex=='while' or lex=='WHILE':
        fileoutput.write("      <WHILE>      \n")
    elif lex=='return' or lex=='RETURN':
        fileoutput.write("      <RETURN>      \n")

def print_operator(lexeme):
    if lexeme=='=':
        fileoutput.write("      <ASSIGN>      \n")
    elif lexeme in ['<', '>', '<=', '>=']:
        fileoutput.write("      <COMPARE>      \n")
    elif lexeme=='==':
        fileoutput.write("      <EQUAL>      \n")
    elif lexeme=='!=':
        fileoutput.write("      <NOTEQUAL>      \n")
    elif lexeme in arth_operator:
        fileoutput.write("      <OP, "+lexeme+" >      \n")
    elif lexeme==';':
        fileoutput.write("      <SEMI>      \n")
    elif lexeme=='(':
        fileoutput.write("      <LPAREN>      \n")
    elif lexeme==')':
        fileoutput.write("      <RPAREN>      \n")
    elif lexeme=='{':
        fileoutput.write("      <LBRACE>      \n")
    elif lexeme=='}':
        fileoutput.write("      <RBRACE>      \n")
    elif lexeme==',':
        fileoutput.write("      <COMMA>      \n")

file=open("test.txt", 'r')
st=file.read()

fileoutput=open("test.out.txt", 'w')
fileoutput.write("      <Lexical Analyzer Table>      \n")
fileoutput.write("                                    \n")
fileoutput.write("                                    \n")

lexeme=[]
state=0

for i, char in enumerate(st):
    lexeme += char
    #white_space는 포함하지 않음
    if lexeme[0] in white_space:
        del lexeme[0]
        continue

    #'-'가 operator일 경우 먼저 write를 하기 위한 함수들
    if (lexeme[0]=='-') and (len(lexeme)==1):
        continue
    if lexeme[0]=='-' and lexeme[1] not in Number:
        print_operator(lexeme[0])
        del lexeme[0]
    elif lexeme[0]=='-' and lexeme[1]=='0':
        print_operator(lexeme[0])
        del lexeme[0]

    #Literal_String DFA
    if lexeme[0]=='"':
        state=transition(Lit_dfa, lexeme)
        #String이 '"'로 끝남
        if state==2:
            lex=lexeme[1:len(lexeme)-1]
            lex="".join(lex)
            fileoutput.write("      <STRING, "+lex+" >      \n")
            state=0
            lexeme.clear()
            continue
        #String이 예상하지 못한 문자로 끝남
        elif state==-1:
            #Error Detection
            data = "      error detacted at " + str(i - len(lexeme) + 2) + "th character      \n"
            fileoutput.write(data)
            break

        #read file이 끝남
        elif i+1==len(st):
            lex="".join(lexeme)
            fileoutput.write("      <STRING, " + lex + " >      \n")
            state = 0
            lexeme.clear()
            continue
    #Identifier DFA
    elif lexeme[0] in alphabet:
        state=transition(Id_dfa, lexeme)
        #ID가 예상치 못한 입력으로 끝남
        if state==-1:
            #Error Detection
            if char not in allwordsID:
                data = "      error detacted at " + str(i - len(lexeme) + 2) + "th character      \n"
                fileoutput.write(data)
                break
            lex = lexeme[0:len(lexeme) - 1]
            lex = "".join(lex)
            #Lexeme이 Keyword나 Type과 일치 시 file에 write
            if lex in keyword or lex in type:
                print_word(lex)
            else:
                fileoutput.write("      <ID, " + lex + " >      \n")
            state=0
            lexeme.clear()
            if char not in white_space:
                lexeme+=char
            else:
                continue
        # read file이 끝남
        elif i+1==len(st):
            lex="".join(lexeme)
            if lex in keyword or lex in type:
                print_word(lex)
            else:
                fileoutput.write("      <ID, " + lex + " >      \n")
            state = 0
            lexeme.clear()
            continue
    #Integer DFA
    elif lexeme[0] in (Number+['-']):
        state=transition(Int_dfa, lexeme)
        #Integer가 숫자가 아닌 입력으로 끝남
        if state==-1:
            #Error Detection
            if char not in allwordsNum:
                data = "      error detacted at " + str(i - len(lexeme) + 2) + "th character      \n"
                fileoutput.write(data)
                break
            lex = lexeme[0:len(lexeme) - 1]
            lex = "".join(lex)
            fileoutput.write("      <INTEGER, " + lex + " >      \n")
            state=0
            lexeme.clear()
            if char not in white_space:
                lexeme += char
            else:
                continue
        # 0 처리, 0이 아닌 정수는 맨 앞이 0일 수 없음
        elif state==3:
            lex = "".join(lexeme)
            fileoutput.write("      <INTEGER, "+lex+" >      \n")
            state=0
            lexeme.clear()
            continue
        # read file이 끝남
        elif i+1==len(st):
            lex="".join(lexeme)
            fileoutput.write("      <INTEGER, " + lex + " >      \n")
            state = 0
            lexeme.clear()
            continue
        #Integer가 음수일 경우, lexeme이 Operator 출력 과정을 거치지 않게 하기위한 코드
        elif state==1 or state==2:
            continue

    #Operator
    #Operator가 2글자 이상일 경우, continue로 lexeme에 모든 문자를 담게한다
    if (i+1) < len(st):
        if (lexeme[0] in ['=', '<', '>', '!']) and st[i+1]=='=':
            continue

    #Operator가 2글자 이상이고 Lexeme에 모두 있을 경우 file에 write
    if len(lexeme) > 1:
        if (lexeme[0] in ['=', '<', '>', '!']) and lexeme[1]=='=':
            lex=lexeme[0]+lexeme[1]
            lex="".join(lex)
            print_operator(lex)
            lexeme.clear()
            continue

    #'!="가 아닌 '!'는 error이므로 error detection
    if lexeme[0]=='!':
        data="      error detacted at "+str(i-len(lexeme)+2)+"th character      \n"
        fileoutput.write(data)
        break

    #그외의 모든 기호들을 file에 write
    if lexeme[0] in alloperator:
        print_operator(lexeme[0])
        del lexeme[0]