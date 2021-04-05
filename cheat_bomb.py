
def password():
    password=['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
    n_col=0
    x=0
    while x==0:
        print(n_col+1 , "coloum  letters: (0 to exit)")
        coloum=input()
        if (coloum=='0'):
            x=1
            break
        right=[]
        for i in coloum:
            for j in password:
                if i==j[n_col]:
                    right.append(j)
                else:
                    pass
        password=right
        right=[]
        n_col=n_col+1
        print(password)	

def wires():
    print('insert colors of cables (r:red w:white b:blue y:yellow n=black)')
    cables=input()
    r=0
    w=0
    b=0
    y=0
    n=0

    for i in cables:
        if i == 'r':
            r=r+1
        elif i == 'w':
            w=w+1
        elif i == 'b':
            b=b+1
        elif i == 'y':
            y=y+1
        elif i == 'n':
            n=n+1
        else:
            pass

    if len(cables)==3:
        if r==0:
            print('cut 2 wire')
        elif cables[2]==w:
            print('last one')
        elif b>=1:
            print('last blue')
        else:
            print('last one')

    elif len(cables)==4:
        if r>=1:
            print('last digit of serial is odd? (y/n)')
            value=input()
            if value=='y':
                print('cut last red')
                return
        if cables[3]=='y' and r==0:
            print ('cut first wire')
        elif b==1:
            print ('cut first wire')
        elif y>1:
            print('cut the last one')
        else:
            print('cut second wire')

    elif len(cables)==5:
        if cables[4]=='b':
            print('last digit of serial is odd? (y/n)')
            value=input()
            if value=='y':
                print('cut fourth one')
                return
        if r==1 and y>1:
            print ('cut first one')
        elif b==0:
            print ('second')
        else:
            print('first')

    elif len (cables)==6:
        if y==0:
            print('last digit of serial is odd? (y/n)')
            value=input()
            if value=='y':
                print('cut third one')
                return
        if y==1 and w>1:
            print('cut fourth')
        elif r==0:
            print('last one')
        else:
            print('fourth')

def botton():
    print('write colour (b:blue w:white y:yellow r:red')
    color=input()
    print('write what is written on the button (a:abort d:detonate h:hold)')
    write=input()
    print('write n batteries')
    n_bat=int(input())
    print('write xy where x is 1 if label CAR is lit; y is 1 if label FRK is lit; 0 otherwise')
    labels=input()

    if color=='b' and write =='a':
        releasing()
    elif n_bat>1 and write=='d':
        print('press and realise')
    elif color=='w' and labels[0]=='1':
        releasing()
    elif n_bat>2 and labels[1]=='1':
        print('press and realise')
    elif color=='y':
        releasing()
    elif color=='r' and write=='h':
        print('press and realise')
    else:
        releasing()

def releasing():
    print('hold press and write what color (b:blue w:white y:yellow 0:otherwise)')
    col=input()
    if col=='b':
        print('release when a digit is 4')
    elif col=='w':
        print('release when a digit is 1')
    elif col=='y':
        print('release when a digit is 5')
    elif col=='0':
        print('release when a digit is 1')
    else:
        print('release when a digit is 1')



def keypass():
    pass

def symonsays():
    pass

def display():
    pass

def memory():
    pass

def morse():
    pass

def complicated_wires():
    pass

def wire_sequence():
    pass

def mazes():
    pass

def others():
    pass

while True:
    print('what minigame give you throuble?\n1: \twires,\n2: \tbotton,\n3: \tkeypass,\n4: \tsymonsays,\n5: \tdisplay,\n6: \tmemory,\n7: \tmorse,\n8: \tcomplicated_Wires,\n9: \twiresequence,\n10: \tMazes,\n11: \tpassword,\n12: \tothers')

    game=input()
    
    if game=='1':
        wires()
    if game=='2':
        botton()
    if game=='3':
        keypass()
    if game=='4':
        symonsays()
    if game=='5':
        display()
    if game=='6':
        memory()
    if game=='7':
        morse()
    if game=='8':
        complicated_wires()
    if game=='9':
        wire_sequence()
    if game=='10':
        mazes()
    if game=='11':
        password()
    if game=='12':
        others()


     

