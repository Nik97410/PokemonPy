from logging import exception
from multiprocessing import set_forkserver_preload
import random
from random import randint
import string


class Pokemon:
    # Définition des attribut de cette classe
    __Energie: int
    __maxEnergie: int
    __Nom: str
    __cycle: int
    __Puissance : int
    __Furie : bool
    __Faible : bool
    Type = ["Feu","Terre","Eau","Electrique"]
    __Dresseur:str

    # Voici les constructeur

    def __init__(self, Nom  ):
        self.__Nom = Nom
        self.__Dresseur = False
        self.__maxEnergie = randint(50, 90)
        self.__Energie = randint(30, self.__maxEnergie)
        self.__cycle = 0
        self.__Puissance = randint(3, 10)
        self.__Furie = False
        self.__Type = random.choice(self.Type)

    def getNom(self):
        return (self.__Nom)

    def getEnergie(self):
        return (self.__Energie)

    def getType (self):
        return (self.__Type)

    def getPuissance(self):
        return (self.__Puissance)

    def getDresseur(self):
        if self.__Dresseur == True:
            return("Je suis un Pokemon sauvage")
        else:
            return ("Le pokemon {} appartient au dresseur {}".format(self.getNom(),self.__Dresseur))
    
    def setDresseur(self):
        if self.__Dresseur == False:
            self.__Dresseur = input("Définir le dresseur : ")
        else:
            self.__Dresseur =True
    
    def sePresenter(self):
        return "Je suis {} et je suis de type {}, j'ai {} point d'energie ({} Max) et une puissance de {}".format(self.__Nom,self.__Type, self.__Energie, self.__maxEnergie, self.__Puissance)

    def Manger(self):
        obtenue = randint(10, 30)
        self.__Energie += obtenue
        if self.__Energie > self.__maxEnergie:
            self.__Energie = self.__maxEnergie
        self.__cycle += 0.5
        return "Votre pokemon a obtenu {} point d'energie son energie est maintenant de {}".format(obtenue, self.__Energie)

    def Vivre(self):
        perdue = randint(40, 50)
        self.__Energie -= perdue
        if self.__Energie < 0:
            self.__Energie == 0
        self.__cycle += 0.5
        return "Votre pokemon a perdu {} point d'energie son energie est maintenant de {}".format(perdue, self.__Energie)

    def isAlive(self):
        if self.__Energie > 0:
            return True
        else:
            return False

    def cycle(self):
        return "Votre pokemon : {} a vécu {} cycles !".format(self.__Nom, self.__cycle)

    def perdreEnergie(self,perte):
        if self.__Energie <= (self.__maxEnergie /4 ) and self.__Faible == False :
            self.__Faible = True
            perte = perte * 1.5

        self.__Energie -= perte
        if self.__Energie <= 0:
            self.__Energie = 0

            
        
        
        
    def attaquer(self, adversaire):
        if self.__Puissance > 1 :
            self.__Puissance -= randint(0,1)
        
        
        if self.__Energie <= (self.__maxEnergie /4 ) and self.__Furie ==False :
            print (self.__Nom,"Pokemon en furie")
            self.__Furie = True
            self.__Puissance= self.__Puissance * 2

        adversaire.perdreEnergie(self.getPuissance())

    def Resister(self):
        try:
            if self.__Energie > (self.__maxEnergie /2):
                libre=(10/0)
        except ZeroDivisionError:
            libre =randint(1,5)
            capture = randint(1,10)
            print(libre)
            print(capture)
            if (libre)==1 or (libre)==2 or (libre)==3 :
                print("Votre Pokemon {} est libre".format(self.getNom()))
            elif (capture)==10 or (capture)==9 or (capture)==8 or (capture)==7 or (capture)==6 or (capture)==5 or (capture)==4 :
                print("Votre Pokemon {} a été capturé".format(self.getNom()))
            else:
                print ("raté {} est donc libre" .format(self.getNom()))

