from blackjack import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from PIL import ImageTk,Image


class Sucelje:
    def __init__(self,boole):
        self.boole = boole
        if boole:
            self.ulogiran = False
            self.root = tk.Tk()
            self.root.title('Blackjack')
            self.root.geometry('500x300+200+200')
            self.root.resizable(0, 0)
            naslov = tk.Label(text="Dobrodošli u Blackjack", font = ('Verdana', 20, 'bold'))
            naslov.place(x=75,y=60)
            prijavagumb = tk.Button(text="Prijava", font=('Verdana', 16,), command=self.Prijava)
            registracijagumb = tk.Button(text="Registracija", font= ('Verdana', 16,), command=self.Reg)
            prijavagumb.place(x=200,y=125)
            registracijagumb.place(x=177,y=175)
            self.root.mainloop()
        if boole == False:
            self.ulogiran = True
            

    def Prijava(self):
        self.prijava = tk.Toplevel(self.root)
        self.prijava.title('Blackjack - Prijava')
        self.prijava.geometry('350x200+275+255')
        self.prijava.resizable(0, 0)
        naslov2 = tk.Label(self.prijava, text="Prijava", font = ('Verdana', 15, 'bold'))
        naslov2.place(x=135,y=20)

        uslabel = tk.Label(self.prijava, text="Username: ", font = ('Verdana', 12 ))
        sifralabel= tk.Label(self.prijava, text="Sifra: ", font = ('Verdana', 12))
        uslabel.place(relx=0.1,rely=0.3)
        sifralabel.place(relx=0.1,rely=0.4)

        self.username = tk.Entry(self.prijava, width = 10)
        self.sifra = tk.Entry(self.prijava, show="*")

        self.username.place(relx=0.4,rely=0.3)
        self.sifra.place(relx=0.3,rely=0.4)
        
        prijavagumb = tk.Button(self.prijava, text="Login", font=('Verdana', 16,), command= self.Log)
        prijavagumb.place(relx=0.4,rely=0.7)

        self.prijava.mainloop()
    def Log(self):
        us = self.username.get()
        sifra = self.sifra.get()
        if Korisnici().ProvjeriUsername(self.username.get(), login=True):
            if Korisnici().Login(us,sifra):
                self.korisnik = Korisnik(us,sifra)
                balance= self.korisnik.getBalance()
                if int(balance)== 0:
                    mb.showerror("Brisanje profila","Stanje na vašem računu je 0, vaš korisnički profil se briše")
                    Korisnici().delUser(us)
                else:
                   mb.showinfo("Uspješna prijava", 'Uspješno ste prijavljeni, ' + us)
                   self.ulogiran = True
                   self.root.destroy()
                   
                   self.KorisnikMenu(self.korisnik)
            else:
                mb.showerror("Neuspješna prijava", "Prijava nije uspješna.")
        else:
            mb.showerror("Nepostojeći korisnik", "Korisničko ime ne postoji.")
                
                    
    def Reg(self):
        self.reg = tk.Toplevel(self.root)
        self.reg.resizable(0, 0)
        self.reg.title('Blackjack - Registracija')
        self.reg.geometry('350x200+275+255')
        naslov2 = tk.Label(self.reg, text="Registracija", font = ('Verdana', 15, 'bold'))
        naslov2.place(x=110,y=20)
        uslabel = tk.Label(self.reg, text="Username: ", font = ('Verdana', 12 ))
        sifralabel= tk.Label(self.reg, text="Sifra: ", font = ('Verdana', 12))
        uslabel.place(relx=0.1,rely=0.3)
        sifralabel.place(relx=0.1,rely=0.4)

        self.usreg = tk.Entry(self.reg, width = 10)
        self.sifrareg = tk.Entry(self.reg, show="*")

        self.usreg.place(relx=0.4,rely=0.3)
        self.sifrareg.place(relx=0.3,rely=0.4)
        
        prijavagumb = tk.Button(self.reg, text="Login", font=('Verdana', 16,), command= self.Regis)
        prijavagumb.place(relx=0.4,rely=0.7)

    def Regis(self):
        us = self.usreg.get()
        sifra = self.sifrareg.get()
        if Korisnici().ProvjeriUsername(us,False):
            mb.showerror("Postojeći korisnik", "Vaše korisničko ime nije valjano ili je već u uporabi. Pokušajte ponovno sa drugim korisničim imenom.")
        else:
           Korisnici().Reg(us,sifra)
           mb.showinfo("Uspješna registracija", "Vaša registracija je uspješna")

    def KorisnikMenu(self,korisnik):
       self.korisnik = korisnik
       self.KM = tk.Tk()
       self.KM.resizable(0, 0)
       self.KM.geometry('700x500+200+200')
       self.KM.title('Blackjack - ' + self.korisnik.username)
       dobrodosli = ("Dobrodošli, " + self.korisnik.username.capitalize() + "!")
       naslov1 = tk.Label(self.KM, text="IZBORNIK", font = ('Verdana', 15, "bold" ), justify = 'center')
       naslov = tk.Label(self.KM, text=dobrodosli, font = ('Verdana', 15 ), justify = 'center')
       naslov.place(x=250,y=50)
       naslov1.place(x=300,y=20)
       iznos = tk.Label(self.KM, text="Iznos na racunu: "  + self.korisnik.getBalance() + '€', font = ('Verdana', 10 ))
       iznos.place(relx=0.7,rely=0.9)
       
    
       gumb1 = tk.Button(self.KM, text="Igraj Blackjack", font=('Verdana', 16,), command= self.Destroy, justify = 'center')
       gumb3 = tk.Button(self.KM, text="Prikaži ljestvicu najbogatijih", font=('Verdana', 16,),justify = 'center', command= self.Ljestvica)
       gumb4 = tk.Button(self.KM, text="Odjava", font=('Verdana', 16,), justify = 'center', command= self.Odjava)
       gumb1.place(x=275,y=100)
       #gumb2.place(x=285,y=200)
       gumb3.place(x=215,y=200)
       gumb4.place(x=310,y=300)
       self.KM.mainloop()
    def Ljestvica(self):
        self.LJ = tk.Toplevel(self.KM)
        self.LJ.resizable(0, 0)
        self.LJ.geometry('350x200+275+255')
        self.LJ.title('Blackjack - Ljestvica')
        ljestvica = Korisnici().Ljestvica()
        naslov = tk.Label(self.LJ, text="Ljestvica najbogatijih", font=('Verdana', 12, 'bold'),justify = 'center')
        naslov.place(x=75,y=10)
        label1=0
        label3=0
        label2=0
        label4=0
        label5=0
        ll = [label1,label2,label3,label4,label5]
        for broj, korisnik in enumerate(ljestvica, 1):
            if broj==6:
                break
            tekst= str(broj) + ".", korisnik[0] + " -> " + korisnik[1] + "€"
            ll[broj-1] = tk.Label(self.LJ, text= tekst, font=('Verdana', 10,), justify = 'center')
            ll[broj-1].place(x=100,y=33*broj)
    def Odjava(self):
        self.ulogiran=False
        self.korisnik= None
        self.KM.destroy()
        sucelje = Sucelje(True)

    def Destroy(self):
        Blackjack(self.korisnik)
        self.KM.destroy()

class Blackjack:
    def __init__(self, korisnik):
        self.korisnik = korisnik   
        self.korisnik.Igranje = True
        if int(self.korisnik.getBalance()) == 0:
            self.korisnik.Igranje = False
            Korisnici().delUser(self.korisnik.username)
            self.korisnik = None
            sucelje=Sucelje(True)
        else:
            
            self.boolIgra = True
            self.ulog = 0
            self.BJ = tk.Tk()
            self.BJ.resizable(0, 0)
            self.BJ.geometry('600x150+200+200')
            self.BJ.title('Blackjack - ' + self.korisnik.username)
            naslov = tk.Label(self.BJ, text ="BLACKJACK", font=('Verdana', 12, 'bold'), justify = 'left')
            naslov.place(x=10,y=10)
            buttonp = tk.Button(self.BJ, text="Povratak na Izbornik", font=('Verdana', 8,), command= self.povratak)
            iznos = tk.Label(self.BJ, text="Iznos: "  + self.korisnik.getBalance() + '€', font = ('Verdana', 10 ))
            iznos.place(relx=0.75,rely=0.85)
            buttonp.place(relx=0.75,rely=0.7)
            buttond = tk.Button(self.BJ, text="DIJELI\nKARTE", font = ('Verdana', 12 ), justify = "center", command=self.Igra)
            buttond.place(x=10, rely=0.65)
            gumb50 = tk.Button(self.BJ, text="+5", font = ('Verdana', 7 ), justify = "center", command=lambda: self.Bet("5"))
            gumb100 = tk.Button(self.BJ, text="+10", font = ('Verdana', 7 ), justify = "center", command=lambda: self.Bet("10"))
            gumb200 = tk.Button(self.BJ, text="+25", font = ('Verdana', 7 ), justify = "center", command=lambda: self.Bet("25"))
            gumb500 = tk.Button(self.BJ, text="+50", font = ('Verdana', 7 ), justify = "center", command=lambda: self.Bet("50"))
            gumbocisti = tk.Button(self.BJ, text="CC", font = ('Verdana', 7 ), justify = "center", command=lambda: self.Bet("CC"))
            gumblista = [gumb50,gumb100,gumb200,gumb500,gumbocisti]
            a=0.15
            for gumb in gumblista:
                gumb.place(relx=a, rely=0.82)
                a=a+0.08
            self.ulog = 0
            self.uloglabel = tk.Label(self.BJ, text="Ulog : " + str(self.ulog), font = ('Verdana', 8, "bold" ),justify = "center")
            self.uloglabel.place(relx=0.15, rely=0.67)
            #gumb50.place(relx= 0.3, rely=0.9)
            #gumb100.place(relx= 0.4, rely=0.9)
    def povratak(self):
        self.BJ.destroy()
        Sucelje(False).KorisnikMenu(self.korisnik)
    def Bet(self,vrijednost):
        if vrijednost == "CC":
            self.ulog= 0
        elif int(int(vrijednost)+int(self.ulog)) <= int(self.ulog):
            self.ulog = int(self.korisnik.getBalance())
        elif int(int(vrijednost)+int(self.ulog)) <= int(self.korisnik.getBalance()):
            self.ulog = int(vrijednost)+int(self.ulog)
        self.uloglabel.configure(text="Ulog : " + str(self.ulog))
            
            
            
        print(vrijednost)

    def Igra(self):
        if self.ulog==0:
            mb.showerror( "Ulog", "Vaš ulog je 0, uložite nešto")
        else:
            self.boolIgra = True
            self.BJ.destroy()            
            self.IgraGUI = tk.Tk()
            self.IgraGUI.resizable(0, 0)
            self.IgraGUI.geometry('600x400+200+200')
            self.IgraGUI.title('Blackjack - ' + self.korisnik.username)
            self.xdj=200
            self.xigrac= 200
            self.placeholder = 0
            naslov = tk.Label(self.IgraGUI, text ="BLACKJACK", font=('Verdana', 12,'bold'), justify = 'left')
            self.stanje = tk.Label(self.IgraGUI, text ="", font=('Verdana', 8), justify = 'left')
            naslov.place(x=10,y=10)
            self.stanje.place(x=10,y=40)
            self.spil = Spil()
            self.spil.promjesajKarte()
            igracKarte,djeliteljKarte = self.spil.djeliKarte()
            self.igracRuka = Ruka(igracKarte)
            self.djeliteljRuka = Ruka(djeliteljKarte)
            self.turn = 1

            self.igracLabel =  tk.Label(self.IgraGUI, text ="IGRAC: " + str(self.igracRuka.total), font=('Verdana' ,12), justify = 'left')
            self.djeliteljLabel = tk.Label(self.IgraGUI, text ="DJELITELJ: " + str(self.djeliteljRuka.karte[0].vrijednost), font=('Verdana', 12 ), justify = 'left')
            self.igracLabel.place(relx=0.41,rely=0.43)
            self.djeliteljLabel.place(relx=0.40,rely=0.38)

            #gumbovi
            self.gumbdalje = tk.Button(self.IgraGUI, text="DALJE", font = ('Verdana', 7 ), justify = "center", command=lambda: self.updateRuka("D"))
            self.gumbstani = tk.Button(self.IgraGUI, text="STANI", font = ('Verdana', 7 ), justify = "center", command=lambda: self.updateRuka("S"))
            self.gumbudvostruci =tk.Button(self.IgraGUI, text="UDVOSTRUČI", font = ('Verdana', 7 ), justify = "center", command=lambda: self.updateRuka("U"))
            self.gumbdalje.place(relx=0.35,rely=0.90)
            self.gumbstani.place(relx=0.45,rely=0.90)
            self.gumbudvostruci.place(relx=0.55,rely=0.90)
            self.generirajKarte(True)
            if self.igracRuka.total==21:
                self.stanje.configure(text=">>> IGRAC >>> BLACKJACK")
                self.updateDjelitelj
                self.korisnik.updateBalance(self.ulog)
                self.Zatvori()

                
       
       


    def updateRuka(self,odabir):
        if self.turn==2 or (self.turn==1 and odabir=="D") or (self.turn==1 and odabir=="S"):
            self.gumbudvostruci.configure(state="disabled")
            
        if odabir== "D":
            novakarta=self.spil.izvuciKartu()[0]
            self.igracRuka.dodajKartu(novakarta)
            load = Image.open(str("images/") + str(novakarta.boja).lower() + "-" + str(novakarta.broj)+ '.jpg')
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.IgraGUI, image=render)
            img.image = render
            img.place(x=self.xigrac, y=210)
            self.xigrac = self.xigrac+20
            
            
            self.igracLabel.configure(text= "IGRAC: " + str(self.igracRuka.total))
            if self.igracRuka.total >21:
                self.boolIgra=False
                self.korisnik.updateBalance(self.ulog*-1)
                self.stanje.configure(text=">>> IGRAC >>> GUBITAK")
                self.Zatvori()
                print(self.igracRuka.total )
            self.turn +=1
        elif odabir == "S":
            self.boolIgra = False
            self.nobust()
        elif odabir == "U" and self.turn==1:
            if self.ulog*2 <= int(self.korisnik.getBalance()):
                self.ulog = self.ulog*2
                novakarta = self.spil.izvuciKartu()[0]
                self.igracRuka.dodajKartu(novakarta)
                load = Image.open(str("images/") + str(novakarta.boja).lower() + "-" + str(novakarta.broj)+ '.jpg')
                render = ImageTk.PhotoImage(load)
                img = tk.Label(self.IgraGUI, image=render)
                img.image = render
                img.place(x=self.xigrac, y=210)
                self.xigrac = self.xigrac+20
                self.boolIgra = False
                self.igracLabel.configure(text= "IGRAC: " + str(self.igracRuka.total))
                self.nobust()
                self.turn +=1
            
        print(odabir)

    def generirajKarte(self,prvipotez):
        if prvipotez:
            for karta in self.igracRuka.karte:
                broj = karta.broj
                boja = karta.boja
                load = Image.open(str("images/")+str(boja).lower() + "-" + str(broj)+ '.jpg')
                print("\\karte\\" + str(boja) + "-" + str(broj))
                render = ImageTk.PhotoImage(load)
                img = tk.Label(self.IgraGUI, image=render)
                img.image = render
                img.place(x=self.xigrac, y=210)
                self.xigrac= self.xigrac+30
            brojdjelitelj = self.djeliteljRuka.karte[0].broj
            bojadjelitelj = self.djeliteljRuka.karte[0].boja
            print(brojdjelitelj,bojadjelitelj)
            load2 = Image.open(str("images/") + str(bojadjelitelj).lower() + "-" + str(brojdjelitelj)+ '.jpg')
            render = ImageTk.PhotoImage(load2)
            img = tk.Label(self.IgraGUI, image=render)
            img.image = render
            img.place(x=self.xdj, y=20)
            self.xdj= self.xdj+20
            


    def updateDjelitelj(self):
            self.djeliteljLabel.configure(text="DJELITELJ: " + str(self.djeliteljRuka.total))
            
            
        
    def Zatvori(self):
        self.gumbdalje.destroy()
        self.gumbstani.destroy()
        self.gumbudvostruci.destroy()
        self.gumbzatvori = tk.Button(self.IgraGUI, text="ZATVORI", font = ('Verdana', 7 ), justify = "center", command=self.povratak2)
        self.gumbzatvori.place(relx=0.45,rely=0.90)
    def povratak2(self):
        self.IgraGUI.destroy()
        Blackjack(self.korisnik)
    def nobust(self):
        brojdjelitelj = self.djeliteljRuka.karte[1].broj
        bojadjelitelj = self.djeliteljRuka.karte[1].boja
        load2 = Image.open(str("images/") + str(bojadjelitelj).lower() + "-" + str(brojdjelitelj)+ '.jpg')
        render = ImageTk.PhotoImage(load2)
        img = tk.Label(self.IgraGUI, image=render)
        img.image = render
        img.place(x=self.xdj, y=20)
        self.xdj= self.xdj+20
        self.gumbdalje.configure(state="disabled")
        self.gumbstani.configure(state="disabled")

        while self.djeliteljRuka.total<17:
            karta = self.spil.izvuciKartu()[0]
            self.djeliteljRuka.dodajKartu(karta)
            load = Image.open(str("images/") + str(karta.boja).lower() + "-" + str(karta.broj)+ '.jpg')
            print("\\karte\\" + str(karta.boja) + "-" + str(karta.broj))
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.IgraGUI, image=render)
            img.image = render
            img.place(x=self.xdj, y=20)
            self.xdj = self.xdj + 20
            self.updateDjelitelj()
            time.sleep(0.2)
            
        self.updateDjelitelj()
        print(self.djeliteljRuka.total)      
        if self.djeliteljRuka.total>21:
            self.stanje.configure(text = " >>> DJELITELJ >>> GUBITAK")
            self.korisnik.updateBalance(self.ulog)
            self.Zatvori()
        elif self.djeliteljRuka.total>self.igracRuka.total:
            self.stanje.configure(text = " >>> IGRAC >>> GUBITAK")
            self.korisnik.updateBalance(self.ulog*-1)
            self.Zatvori()
        elif self.djeliteljRuka.total<self.igracRuka.total:
            self.stanje.configure(text = " >>> IGRAC >>> POBJEDNIK")
            self.korisnik.updateBalance(self.ulog)
            self.Zatvori()
        elif self.djeliteljRuka.total==self.igracRuka.total:
            self.stanje.configure(text = " >>> IZJEDNAČENO")
            self.Zatvori()

        
    
sucelje = Sucelje(True)
podaci = Korisnici()
#sucelje = Sucelje()

#podaci = Korisnici()
#sucelje = Sucelje()
