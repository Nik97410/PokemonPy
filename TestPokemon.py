import math
from Pokemon import Pokemon


# Définition de p1
p1 = Pokemon(input("Veillez saisir le nom de votre Pokemon :") )

# Puis on affiche les données qui ont été attribué a p1

if __name__ == "__main__":
    
    p1.setDresseur()
    print(p1.sePresenter())
    print(p1.getDresseur())

# print(p1.Manger())
# print(p1.Vivre())
# print(p1.isAlive())

#   Exo 1.8
# while (p1.getEnergie()) > 0:
#     print(p1.sePresenter())
#     print(p1.Manger())
#     print(p1.sePresenter())
#     print(p1.Vivre())

#     print(p1.cycle())
#     break

# Partie 2
