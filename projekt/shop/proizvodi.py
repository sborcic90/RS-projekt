#definirajte klasu Proizvod s atributima naziv , cijena i dostupna_kolicina . Dodajte metodu ispis koja će ispisivati sve atribute proizvoda

class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
    
    def ispis(self):
        return f"{self.naziv} ima cijenu {self.cijena} i količinu {self.dostupna_kolicina}"
    
#definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu skladiste .
   

skladiste= []

def dodaj_proizvod(proizvod):
        skladiste.append(proizvod)

proizvod=Proizvod("Mlijeko", 1, 1000)
proizvod1=Proizvod("Kruh", 2, 500)

dodaj_proizvod(proizvod)
dodaj_proizvod(proizvod1)

for proizvod in skladiste:
    print(proizvod.ispis())