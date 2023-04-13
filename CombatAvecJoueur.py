
from argparse import Action
from Pokemon import Pokemon


# Définition de p1 
p1 = Pokemon(input("Player 1 : Nommez votre Pokemon :"))
p2 = Pokemon(input("Player 2 : Nommez votre Pokemon :"))
r=0
# Puis on affiche les données qui ont été attribué a p1

if __name__ == "__main__":
    print("------------------------------------------")
    print("Player 1 :",p1.sePresenter())
    print("Player 2 :",p2.sePresenter())
    print("------------------------------------------")
    while p1.isAlive() == True and p2.isAlive() == True :
        print("------------------------------------------")
        r=r+1
        print ("round numéro :" ,r)
        #Pokemon 1
        Action = int (input(" Player 1 :Attaquer (1) et Manger (0) :"))
        if Action != 1 and Action != 0 :
            Action = int (input(" Veuillez saisir :Attaquer (1) et Manger (0) :"))
        elif Action == 1 :
            p1.attaquer(p2)

        else :
            p1.Manger()
    #Pokemon 2
        Action = int (input(" Player 2 :Attaquer (1) et Manger (0) :"))
        if Action != 1 and Action != 0 :
            Action = int (input(" Veuillez saisir Attaquer (1) et Manger (0) :"))
        elif Action == 1 :
            p2.attaquer(p1)
        else :
            p2.Manger()

        print("Etat des pokemon : ")  
        print("Player 1 :",p1.sePresenter())
        print("Player 2 :",p2.sePresenter())    
        
    if p1.isAlive() == False and p2.isAlive() == False :
        print ("Il y a match Nul au bout de : ",r ,"round !!!!")
    elif p1.isAlive() == True :
        print ("Le vainqueur est :",p1.getNom() , "au bout de : ",r ,"round !!!!")
    else:
        print ("Le vainqueur est :",p2.getNom() , "au bout de : ",r ,"round !!!!")