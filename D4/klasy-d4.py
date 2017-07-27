'''
class PierwszaKlasa:
    def _init_(self, x,y):
        self.x = x
        self.y = y 
        self.dodaj()
        
    
    def witaj(self): 
        print('witaj w metodzie klasy')
    def dodaj(self, x, y):
        self.x = x
        self.y = y 
        return self.x + self.y 
    def odejmowanie(self):
        print("odejmowanie")
        return self.x - self.y

obiekt1 = PierwszaKlasa()
obiekt1.witaj
print(obiekt1.dodaj(4, 5))
print(obiekt1.odejmowanie())


obiekt2 = PierwszaKlasa()
obiekt2.witaj()
print(obiekt2.dodaj)
obiekt1.witaj()
'''
#p75-------------------------------------------------------------------------------------------------------------------------
#Napisz program, który posłuży do obliczania BMI zawodnika
#Utwórz klasę Zawodnik zawierającą metodę do obliczania BMI
#Utwórz obiekt reprezentujący zawodnika
#Wywołaj metodę klasową, która zwróci wartość BMI 
'''
class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost): 
        self.imie = imie 
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.bmi = self.waga / (self.wzrost/100)**2

    def __str__(self): 
        return "BMI dla " +self.imie+ " " +self.nazwisko+ "  wynosi: "+str(self.bmi)
        
z1 = BMI("Michal", "Kruczkowski", 100, 180)
print(z1.bmi)
print(z1)

z2 = BMI("Michal", "Kruczkowski", 198, 180)
print(z2)
'''
#print(66/(184/100)**2)

#print(100 / (187/100)**2)
#print(2**3)
#p-------------------------------------------------------------------------------------------------------------------------

'''
class Sklep: 
    def __init__(self, towar, cena, ilosc):
        self.towar_klasa = towar
        self.cena_klasa = cena
        self.ilosc_klasa = ilosc
    def zapłata(self):
        do_zaplaty = self.cena_klasa * self.ilosc_klasa
        return do_zaplaty
        
zakup1 = Sklep('chelb', 3.99, 4) 
print(zakup1.towar_klasa)
print(zakup1.cena_klasa)
print(zakup1.ilosc_klasa)
zakup1.zaplata()
print(zakup1.do_zaplaty)
'''

'''
zakup1 = Sklep('chlyb', 3.99, 5)
print(zakup1.towar_klasa)
print(zakup1.cena_klasa)
print(zakup1.ilosc_klasa)
'''
        
#p78-------------------------------------------------------------------------------------------------------------------------
#Napisz program lotto, który losuje bez zwracania 6 spośród 49 liczb i wypisuje je na ekran.

import random 
class Lotto: 
    def __init__ (self): 
        self.Tab = (random.sample(range(1,50),6))
    def __del__(self): 
        del self.Tab
        
los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()
