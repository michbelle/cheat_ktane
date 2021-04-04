
def password():
    password=['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
    n_col=0
    x=0
    while x==0 :
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
    pass

def botton():
    pass

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


     

