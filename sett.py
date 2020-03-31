L = {'king' , 'hirozn' , True , 47 , "hola" }

K = set (L)
again = 'y'
while again == 'y': 
    S = input("Entre name to check it : ")
    if S in L :
        print ('yes it\'s here')
    else :
        print ('Name or number , it\'s not exciset')
    
    y = "y"
    n = "n"
    e = input ('You want to add a new name or number in this list , type (y/n) :' )
################################
    if e == y :
        new = input ('Entre new name : ')
        K.add(new)
        print ("A new name has been entered , Done " )
    elif e == n :
        print ('No name to added , Thank you'  )
    else :
        print (' "Wrong entry , please type (y/n)" ')

    y1 = "y"
    n1 = "n"
    e1 = input(' do you want see list... type (y/n) : ')
    if e1 == y1:
        print(K)
    elif e1 == n1 :
        print ('Ok no list to show ')
    else :
        print ( 'entry , please type yes or no ')
    again = input (' Do you want to use again (y/or type any key to exit ) : ')
exit()

    
input ('Entre to exit')
