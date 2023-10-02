import random
import os
import time
import re

class Korisnici:
    """ Upravljanjem bazom podataka, brisanje, provjera korinsickih podataka."""
    def __init__(self,baza={},imena=[]):
        with open('db.txt', 'r') as korisnici:
            for user in korisnici:
                (key, val) = user.split(':')
                baza[key] = val
                ime= user.split(':')
                imena.append(ime[0])
        self.baza = baza
        self.korisnici = imena

    def Reg(self,username,password):
        startpoeni = 100
        with open('db.txt', 'a') as korisnici:
            korisnici.write(str(username) + ":" + str(password) + "\t" + str(startpoeni) + "\n")

    def delUser(self,username):
        self.baza.pop(username)
        self.spremiBazu()
    
    def spremiBazu(self):
        with open('db.txt', 'w') as korisnici:
            for x, y in self.baza.items():
                y = y.rstrip().split("\t")
                korisnici.write(x + ":" + y[0] + "\t" + y[1] + "\n")
    
    def Login(self,username,password):
        data = self.baza.get(username)
        try:
            data = data.rstrip().split("\t")
        except AttributeError:
            print("Došlo je do greške.")
        if data[0] == password:
            return True
    
    
    def ProvjeriUsername(self,username,login):
        if login==True:
            if username in self.korisnici:return True
            else: return False
        if login==False:
            if bool(re.match(r'^[\w.-]+$', username)):
                if username not in self.korisnici: return False
                else: return True
            else:
                return True
    
    def Ljestvica(self):
        poredak=[]
        for x, y in self.baza.items():
            y= y.rstrip().split("\t")
            podaci= [x,y[1]]
            poredak.append(podaci)
        poredak.sort(key= lambda user: int(user[1]), reverse=True)
        return poredak

class Korisnik:
    """ Klasa Korisnik predstavlja korisnika u sustavu i metode za upravljanjem pojedninacnih korisnickih racuna. 
    Povezuje klasu Korisnici i Blackjack za upravljanje novcem """
    def __init__(self,username,password):
        self.username= username
        self.password= password
        self.Igranje= False
        
    def getBalance(self):
        data= Korisnici().baza.get(self.username)
        data= data.rstrip().split("\t")
        return data[1]
    def updateBalance(self,updatedAmount):
        k = Korisnici()
        data= k.baza.get(self.username)
        data = data.rstrip().split("\t")
        k.baza[self.username] = data[0] + '\t' + str(int(data[1])+int(updatedAmount)) + '\n'
        k.spremiBazu()
    ### odjava,


class Karta:
        
    def __init__(self,boja,broj,value):
        self.boja = boja
        self.broj = broj
        self.vrijednost = value
        
    def __str__(self):
        return self.boja + " " + self.broj

class Spil:
    """
    Metode za spil , generacije spilova 
    """
        
    def __init__(self):
        self.spil = []
        self.rukaIgrac = []
        self.rukaDjelitelj = []
        for boja in Boje:
            for broj,vrijednost in Broj.items():
                self.spil.append(Karta(boja,broj,vrijednost))
        
    def promjesajKarte(self):
        random.shuffle(self.spil)
        
    def djeliKarte(self):
        self.rukaIgrac = random.choices(self.spil, k=2)
        self.izbaciKarteSpil(self.rukaIgrac)
        self.rukaDjelitelj = random.choices(self.spil, k=2)
        self.izbaciKarteSpil(self.rukaDjelitelj)
        return self.rukaIgrac, self.rukaDjelitelj
    def izvuciKartu(self):
        self.novaKarta = random.choices(self.spil, k=1)
        self.izbaciKarteSpil(self.novaKarta)
        return self.novaKarta

    def izbaciKarteSpil(self, karte):
        for karta in karte:
            try:
                self.spil.remove(karta)
            except ValueError:
                pass

class Ruka:
    """ Racuna vrijednost ruke i mijenja vrijednost """
    def __init__(self,karte):
        self.karte = karte
        self.total = 0
        for karta in karte:
            if karta.broj != "As":
                self.total += karta.vrijednost
            if karta.broj == "As" and self.total<=10:
                self.total += karta.vrijednost
            elif karta.broj == "As" and self.total>=11:
                self.total += 1                        

            
    
    def dodajKartu(self,karta):
        self.karte.append(karta)
        if karta.broj != "As":
            self.total += karta.vrijednost
        if karta.broj == "As" and self.total<=10:
            self.total += karta.vrijednost
        if karta.broj == "As" and self.total>=11:
            self.total += 1

               
Boje = ('Pik', 'Herc', 'Kara', 'Tref')  
Broj = {'Dvojka':2,"Trojka":3,"Četvorka":4, "Petica":5, "Šestica":6, "Sedmica":7, "Osmica":8, "Devetka":9, "Desetka":10, "Dečko":10, "Baba":10, "Kralj":10, "As":11}

