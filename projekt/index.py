"""print("Hello")

a = 3

print(a)
print(type(a))
a, b, c= 1, 2, 3
print("Rezultat je:", a+b+c)

print("Rezultat je:" + str(a+b+c))

a = float(input("Unesite prvi broj: "))

b = float(input("Unesite drugi broj: "))

operacija =input("Unesite operaciju: ")

if operacija=="+":print(f"Rezultat zbrajanja je: {a+b}")
elif operacija=="-":print(f"Rezultat oduzimanja je: {a-b}")
elif operacija=="*":print(f"Rezultat množenja je: {a*b}")
else :print(f"Rezultat djeljenja je: {a/b}")"""

#Napišite program koji će izračunati faktorijel broja#

"""n = int(input("Unesite broj: "))
#print(n)#
izracun=1

for i in range(1, n+1):
    izracun*=i
    print(f"Rezultat broja {i} je: {izracun}")"""
    
    
"""n = int(input("Unesite broj: "))
#print(n)#
izracun=1
i=1

while i<=n:
    izracun*=i
    i+=1
    print(f"Rezultat broja {i} je: {izracun}")"""
   
"""broj = 0
while broj < 5:
    broj +=2
    print(broj) """
    
"""def zbroj_razlika(a, b):
    zbroj = a + b
    razlika = a - b
    return zbroj, razlika

z, r = zbroj_razlika(5, 3)
print(z,r)"""

lozinka = input("Unesite lozinku: ")

def provjera_lozinke(lozinka): 
    
    def broj_znakova(lozinka):
        if 8 <= len(lozinka) <=15:
            print ("Lozinka ima dovoljan  broj znakova!")
        else: 
            print("Lozinka mora sadržavati 8 do 15 znakova!")
    broj_znakova(lozinka)
    
    def sadrzi_broj_slovo(lozinka):
        abeceda_velika = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        brojevi = "1234567890"
        
        ima_veliko_slovo = any(slovo in lozinka for slovo in abeceda_velika)

        ima_broj = any(broj in lozinka for broj in brojevi)

        if ima_veliko_slovo and ima_broj:
            print("Lozinka sadrži barem jedno veliko slovo i jedan broj!")
        else:
            print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj!")
    sadrzi_broj_slovo(lozinka)
    
    def sadrzi_rijec(lozinka):
        rijec="lozinka"
        rijec1="password"
        if rijec in lozinka and rijec1 in lozinka:
            print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'") 
        else:
            print("Lozinka je ispravna!")
    sadrzi_rijec(lozinka)
    
    def provjera(lozinka):
        if broj_znakova and sadrzi_broj_slovo and sadrzi_rijec:
            print("Lozinka je jaka!")
        else:
            print("Lozinka nije jaka!")    
    provjera(lozinka)     
             
provjera_lozinke(lozinka)