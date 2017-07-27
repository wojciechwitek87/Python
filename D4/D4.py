# -*- coding: utf-8 -*-

#p74----------------------------------------------------------------------------------------------------------------------------
#Zdefiniuj funkcję, która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).
'''
def suma (*arg):
    suma = 0
    ave = 0 
    for v in arg:
        suma = 0
        ave = 0
        suma += v 
        ave = suma/len(arg)
    return ave 
print(suma(2, 3, 4))
print(suma()) 
'''
#p74(002)-------------------------------------------------------------------------------------------------------------------------
# Napisz funkcję, która będzie rysowała wykres w trybie tekstowym poprzez wybrane przez użytkownika znaczki ( domyślnie *) dla 10 wartości, które użytkownik poda z klawiatury lub wybierze opcję losowo generowanych wartości.

#in --> znak (default*)
#in -10-> wartosc (0-9) 


#>>>>>>>>>>DO DOKONCZENIA BO FAJNE!<<<<<<<<<<<
'''
symbol = raw_input('wybierz znak rysowania i wprowadz z klawiatury, inaczej domyślnie /*/: ')
print('manualnie wprowadzanie wartości - domyslnie')
no = raw_input('wcisnij R by wartosci generowac losowo w zakresie 1-100: ') 

def wykres(znak = '*', ilosc = 10): 
        i = 0
        wartosc = [] 
        
        if (no == 'R'):
                while (i < ilosc):
                        if (znak == ''):
                                wykres('*', 5)
                        else:
                                wartosc.append(random.randomrange(0,10))                       
                        i += 1                
        elif (no != 'R'):
                while (i < ilosc):
                        if (znak == ''):
                                wykres('*', 5)
                        else:
                                wartosc.append(int(raw_input('podaj kolejna wartosc: ')))
                        i += 1
        for v in wartosc: 
                print(znak * v)
wykres(symbol, 5)
'''
#^^^>>>>>>>>>>DO DOKONCZENIA BO FAJNE!<<<<<<<<<<<^^^^

#p74(005)-------------------------------------------------------------------------------------------------------------------------
#Napisz funkcję generującą kod HTML dla napisu:<span style="color: wartość; font-size: wartość; font-weight: wartość“>napis</span>
#-Użytkownik może podać wartości poszczególnych parametrów, jeśli tego nie zrobi przypisywane są wartości domyślne.

'''
def HTML_export(napis, color = 'black', size = '12px', weight = '5px'):
    
    return '<span style="color: '+color+'; font-size: '+size+'; font-weight: '+weight+' “>'+napis+'</span>'
print(HTML_export('Witaj w html'))

color = 'white'

licznik = 0 
licznik_b = 0 
licznik_w = 0 
def naprzemian(): 
    global color
    global licznik 
    global licznik_b
    global licznik_w
    licznik += 1
    if(color == 'white'): 
        color = 'black'
        licznik_b += 1 
        
    elif(color == 'black'):
        color = 'white'
        licznik_w += 1 
        
    return color

print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(licznik)
print(licznik_b)
print(licznik_w)
'''
#p74(120)-------------------------------------------------------------------------------------------------------------------------
#Napisz funkcję do obsługi zdarzeń użytkownika, która będzie pytać co chce wykonać:
#     Dodawanie dwóch liczb  Odejmowanie dwóch liczb  Wyjść z programu
#Po wykonaniu dodawania lub odejmowania funkcja powinna zwów zapytać coużytkownik chce zrobić
'''
def dodawanie (a,b): 
    return a+b 
def odejmowanie (x,y): 
    return x-y 
def menu2():
    dec = ""
    while(dec != 'q'): 
        dec = raw_input('(+) for + / (-) for - / (q) for Q ')
        if (dec == '+'): 
            print('suma= ', dodawanie(int(raw_input("a= ")),int(raw_input("b= "))))
        elif(dec == '-'):
            print('roznica= ', odejmowanie(int(raw_input("a= ")),int(raw_input("b= "))))
        elif(dec != '+' and dec != '-' and dec != 'q'):
            print ('zly wybor')
        

menu2()
'''
#p74(240)-------------------------------------------------------------------------------------------------------------------------
#Napisz funkcję, która będzie sumowała wszystkie te elementy tablicy które są większe od 5.
#Niech funkcja zwraca wartość tej sumy.


def wprowadz(): 
    tab = []
    i = 't'
    print('Wprowadz elementy (enter) - koniec wprowadzania')
    while(i! = ''):
        i = input(' ')
        if(i != ''):
            while True: 
                try: 
                    i = float(i)
                    break
                except ValueError: 
                    print('error! podaj liczbe')
                    i = input(' ') 
            tab.append(i)
        elif(i == ''): 
            print('wprowadzanie zakonczone')
            print(tab)
            return tab 
        
def wypisz5(limit, lista):
    print('filtruje elementy wieksze od: ' + str(limit))
    for v in lista: 
        if (v >= limit): 
            print(v, end=' ')

wypisz5(int(raw_input('podaj limit odciecia: ')), wprowadz())