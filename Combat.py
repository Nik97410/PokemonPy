
from Pokemon import Pokemon


# Définition de p1 
p1 = Pokemon("plantebizzard")
p2 = Pokemon("carafdo")
r=0
# Puis on affiche les données qui ont été attribué a p1

if __name__ == "__main__":
    print(p1.sePresenter())
    print(p2.sePresenter())
    while p1.isAlive() == True and p2.isAlive() == True :
        print("------------------------------------------")
        r=r+1
        print ("round numéro :" ,r)
        p1.attaquer(p2)
        p2.attaquer(p1)
        print(p1.sePresenter())
        print(p2.sePresenter())
        print("------------------------------------------")
    if p1.isAlive() == False and p2.isAlive() == False :
        print ("Il y a match Nul au bout de : ",r ,"round !!!!")
    elif p1.isAlive() == True :
        print ("Le vainqueur est :",p1.getNom() , "au bout de : ",r ,"round !!!!")
    else:
        print ("Le vainqueur est :",p2.getNom() , "au bout de : ",r ,"round !!!!")