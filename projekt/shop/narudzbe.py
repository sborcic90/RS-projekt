# narudzbe.py

# Definicija klase Narudzba
class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    # Metoda koja ispisuje sve naručene proizvode, količine i ukupnu cijenu
    def ispis_narudzbe(self):
        proizvodi_info = []
        for proizvod in self.naruceni_proizvodi:
            proizvodi_info.append(f"{proizvod['naziv']} x {proizvod['narucena_kolicina']}")
        proizvodi_str = ', '.join(proizvodi_info)
        return f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur"

# Lista koja će pohranjivati sve narudžbe
narudzbe = []

# Funkcija koja pravi narudžbu s uvjetima
def napravi_narudzbu_s_uvjetima(proizvodi):
    if not isinstance(proizvodi, list):
        raise ValueError("Naruceni proizvodi mora biti lista!")
    
    if len(proizvodi) == 0:
        raise ValueError("Lista proizvoda ne smije biti prazna!")

    for proizvod in proizvodi:
        if not isinstance(proizvod, dict):
            raise ValueError("Svaki element u listi mora biti rječnik!")
        if not all(k in proizvod for k in ['naziv', 'cijena', 'narucena_kolicina']):
            raise ValueError("Svaki proizvod mora sadržavati ključeve: naziv, cijena, narucena_kolicina")
    
    # Provjera dostupnosti proizvoda
    for proizvod in proizvodi:
        if proizvod['stanje'] == 0:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None
    
    # Izračun ukupne cijene narudžbe
    ukupna_cijena = sum(proizvod['cijena'] * proizvod['narucena_kolicina'] for proizvod in proizvodi)
    
    # Kreiranje instance klase Narudzba
    nova_narudzba = Narudzba(proizvodi, ukupna_cijena)
    
    # Pohrana u listu narudzbi
    narudzbe.append(nova_narudzba)
    print("Narudžba uspješno dodana.")
