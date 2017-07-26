# -*- coding: utf-8 -*-
import random
# Dzień 2 ---------------------------------------- 
'''
literki = {'a' : 'A', 'b' : 'B', 'c' : 'C'} 
print(literki) 
print(len(literki)) 
print(literki['a'], literki['b'])
literki['c'] = 'napis' 
print(literki['c'])
print(literki.keys(), literki.values())
literki['d'] = 'D' 
del literki['c'] 
literki[2] = 'abc' 
print(literki)
to_str = str(literki)
print(to_str[0], to_str[1])
'''

#p44------------------------------------------------------------ 
'''
key1 = raw_input('wpisz słownie cyfrę z przedziału 1-5: ') 
to_dec = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
#print(key1.capitalize() +' w postaci liczby dziesiętnej to: ' +str(to_dec[key1])) 
'''
#p47------------------------------------------------------------ 
'''
to_rom = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
print(key1.capitalize() +' w postaci liczby arabskiej to: '+str(to_dec[key1]) + ' a, w postaci rzymskiej to: '+str(to_rom[to_dec[key1]]))
'''
#p48------------------------------------------------------------ 
'''
key_1 = raw_input('>>Co chcesz kupić?? Chleb, masło czy może dżem...?<< ') 
key_2 = int(raw_input('ile sztuk tego towaru? '))
produkty_id = {'chleb':'1x', 'masło':'2x', 'maslo':'2x', 'dżem':'3x', 'dzem':'3x'} 
cena_n = {'1x':1.99, '2x':3.99, '3x':5.99} 
print('do zapłaty: ' +str(round(cena_n[produkty_id[key_1]]*key_2))+'zł ('+str(round((cena_n[produkty_id[key_1]]*key_2)*1.23,2))+' zł brutto)') 
'''
#p48------------------------------------------------------------ 
'''
ksztalty = set(['kolo', 'kwadrat', 'trojkat']) 
ksztalty.add('okrag')
ksztalty.discard('kolo')
print(ksztalty) 
okragle = set(['okrag']) 
print(len(ksztalty), len(okragle)) 
print(ksztalty.issubset(okragle))
print(ksztalty.issuperset(okragle))

#operacje na zbirach
print(ksztalty) 
print(okragle)
print(ksztalty | okragle) 
print(ksztalty & okragle)
print(ksztalty - okragle)
print(ksztalty ^ okragle)
'''
#p49------------------------------------------------------------ 

"""
s = set()
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
l = list(s)
print(l[:6])
"""
#instrukcja_warunkowa_if-----------------------------------------
'''
a = int(raw_input('podaj liczbę: ')) 
if(a%2 == 0): 
    print('liczba '+str(a)+' jest parzysta') 
    if(a> = 10):
        print('liczba '+str(a)+ 'jest parzysta i wieksza lub rowna 10')
    else: 
        print('liczba '+str(a)+ 'jest parzysta i mniejsza 10')
else: 
    print('liczba ' +str(a)+ "jest nieparzysta")
print('jestem już za instrukcją if') 
'''

#>><< 
"""
a = int(raw_input('podaj liczbę: ')) 
if(a%2 == 0 and a>=10): 
        print('liczba '+str(a)+ 'jest parzysta i wieksza lub rowna 10')
elif (a%2 == 0 and a < 10):
        print('liczba '+str(a)+ 'jest parzysta i mniejsza 10')
else: 
        print('liczba ' +str(a)+ "jest nieparzysta")
print('jestem już za instrukcją if') """

#p53------------------------------------------------------------ 
"""
if(0): 
        print(bool(0))
if(1):
        print(bool(1))
if(2): 
        print(bool(2))
if(3):
        print(bool(3))
if(4):
        print(bool(4))        
        """

#p54------------------------------------------------------------ 
'''
lista = [1,2,3,4,5,6,7,8,9]
index = int(raw_input('podaj indeks do liczby ktora chces zwyswietlic: '))
'''"""           
if (index >= 0 and index <=(len(lista)-1)):
             print('liczba znajduje sie przedziale') 
             print(lista[index])
else: 
             print('poza skala')
"""
             
#p55------------------------------------------------------------ 
'''
if(lista[0]>0 and lista[1]>0):
    print('oba >0')
elif(lista[0]>0 and lista[1]<0):
    print('pierwszy>0 drugi<0')
elif(lista[0]>0 and lista[1]>0):
    print('pierwszy<0 drugi>0')
else: 
    print('oba <o') 
    '''
#------------------
'''
A = set([1,2,3,4,5])
B = set([1,2,3,4])

if(A == B): 
    print('zbiory rowne') 
elif(A.issuperset(B)):
    print('A jest nadzwbiorem B')
elif(B.issuperser(A)):
    print('B jest nadzbiorem A') 
else: 
    print('f_it')
    '''

'''
lista = [1,2,3,4,5,6,7,8,9]
i = (len(lista)-1) 
while(i >= 0):
    if(lista[i]%2 == 0):
        print("index: " +str(i)+ "\t Wartosc: " +str(lista[i]))
    i -=1 
else: 
    print('jestem w pesie') 
#która z liczb jes wieksz ai o ile 

a = 14 
b = 15 
#print() if (a >= b) else print() 
'''
'''
lista = [1,2,3,4,5,6,7,8,9]

for var in lista: 
    print('wartosc: ' +str(var))
lista.append(15)    
for index, var in enumerate(lista): 
    print('index: ' +str(index)+ "\twartosc: " +str(var))
    
Sl = {'a':1, 'b':2, 'c':3}
for k in Sl: 
    if(Sl[k] >= 2): 
        print(k, Sl[k])
        
        
s1 = range(100)
#print(s1)
for i in s1: 
    print(i)
    
for j in range(15,25):
    print(j)
    
for k in range(0,100):
    print('Wynik: %4i%6i%8i' % (k, k**2, k**3)) 
'''    
'''
for x in range(5,100,10):
    print("Pierwiastkiem liczby %2i jest %5.3f" % (x,x**0.5))    
    '''

#p57------------------------------------------------------------ 
'''
sklep_produkty = {"monitor": 1, "klawiatura": 2, "mysz": 3}
produkty_cena = {1: 1500, 2: 400, 3: 200}
produkty_dostepnosc = {1: 5, 2: 5, 3: 15}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = raw_input("Wybierz towar: ")
    zamowienie_ilosc = int(raw_input("Podaj ilosc zamawianego produktu: "))
    for k in sklep_produkty:
        if (zamowienie in sklep_produkty.keys()):
            if(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]] >= zamowienie_ilosc):
                print("Produkt dostępny: " + k)
                print("Zamawiasz: " + str(zamowienie_ilosc) + ' szt')
                suma += zamowienie_ilosc* produkty_cena[sklep_produkty[k]]    
            elif(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]] < zamowienie_ilosc):
                print("Produkt dostępny: " + k)
                print("Jest dostępne tylko: " + str(produkty_dostepnosc[sklep_produkty[k]]) + ' szt')        
        else:
            print("Brak produktu w sklepie")
            break
    i = raw_input("czy chcesz zamawiać dalej? (t/n)")
print("Do zapłaty: "+ str(suma))
'''

#p60------------------------------------------------------------ 
"""
li = raw_input('Podaj ciag liczb do konwersji na tekst: ')
key = {"0":'zero', '1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'piec', '6':'szesc', '7':'siedem', '8':'osiem', '9':'dziewiec'}
i = 't'
res = [] 
while( i == 't'):
    if(li.isdigit()): 
        res.append(key[li])
    else: 
        print('podana wartosc nie jest cyfra')
    i = raw_input('czy chcesz dalej wpisywac t/n: ')
for i in res:
    print(i) 
    """
'''    #<<do skonczenia
#p61------------------------------------------------------------ 
line = range(1,11) 
n = 1 
while (n<=10): 
    print('%3i|%3i|%3i|%3i|%3i|%3i|%3i|%3i|%3i|%3i|' % (n*line[0], n*line[1], n*line[2], n*line[3], n*line[4], n*line[5], n*line[6], n*line[7], n*line[8], n*line[9]))
    n +=1

#p61------------------------------------------------------------ 

line = range(1,10,2) 
i = len(line) -1 
while(i >=0): 
    if(i == 0):
        print(np[i]**2)
    else: 
        print(np[i]**2, end=',')
    i-=1
    
'''
 
 #p63------------------------------------------------------------ 
'''
 #print(liczymy x do y)
x = int(raw_input('podaj x: '))
y = int(raw_input('podaj y: '))
res = 1 
i = 1 
while(i<= y):
  res = res*x
  i +=1 
print(res)
'''
#p------------------------------------------------------------ 
#oblicz sume ciagu geometrycznego
'''
#n = int(raw_input('podaj n:   '))
#a_1 = float(raw_input('podaj a_1: '))
#q = float(raw_input('podaj q:   ')) 
n = 3 
a_1 = 3
q = 2
i = 0 
s = 0 
l = []
while(i < n):
 s += a_1*(q**i)
 l.append(a_1*(q**i))
 i += 1
>>>>>> print('%10s %-15.2f' % ('Suma: ', s)) #, 10  (s) oznacza string,10 pozycji na sume odsuniecie o 15 pozycji 2 to miejsca po przecinku 
for v in enumerate(l):
 if(i == 0):
 
 #print('Ostatni wyraz: ',a_1*(q**(n-1)))

'''

#p------------------------------------------------------------ 
''' 
txt = raw_input('podaj napis: ') 
szukaj = raw_input('podaj szukana fraze: ')
i = 0 
licznik = 0 
while (i <= len(txt)-1):
 if(txt[i] == szukaj): 
  print('znalezieono: ', szukaj, 'na pozycji', i+1)
  licznik += 1 
 i += 1 
print('znaleziono ', licznik, 'razy')
'''
#-----------------------------
'''
txt = raw_input('podaj napis: ') 
szukaj = raw_input('podaj szukana fraze: ')

ilosc = len(txt) - len(szukaj) + 1 
licznik = 0 
i = 0 
while (i < len(txt)):
 tab = txt[i:i + len(szukaj)]
 if (tab == szukaj):
  print('znalezieono: ', szukaj, 'na pozycji', i+1)
  licznik += 1 
  i = i + len(szukaj)
  
 else:
  i += 1 
print('znaleziono ', licznik, 'razy') 
'''
#p------------------------------------------------------------ 
# C to F
'''
#F = (C*1.8)+32
start = int(raw_input('start C: '))
stop = int(raw_input('stop C: '))
step = int(raw_input('step: '))
if((stop - start) %  step == 0):   
  C = range(start,stop + step,step)
else:
  C = renge(start, stop, step)
print('%5s | %5s' % ('C', 'F'))
i=len(C)-1
while(i >= 0):
  if(C[i] == 0):
    print('---------------')
    print('%5i | %5.1f' % (C[i], (C[i]*1.8)+32))
    print('---------------')
  else:
    print('%+5i | %+5.1f' % (C[i], (C[i]*1.8)+32))
  i -= 1
#for i in range(40,-20,5): 
#
'''
#p------------------------------------------------------------ 

D = ['3', '4', '5'] 
i = "x"
O = []
print('podaj oceny do wprowadzenia: ')
while(i != ""):
 i = raw_input(' ')
 if(i in D):
  O.append(float(i))
 elif(i == ''):
  print('zakonczyles wprowadzanie ocen ')
 else:
  print('zla ocena')
sr = 0
if(len(O) != 0):
 for i in O:
  sr += i
print'srednia ocen: ', round(sr/len(O),2)