# main.py

# Učitavanje modula iz paketa shop
from shop.narudzbe import napravi_narudzbu_s_uvjetima, narudzbe

# Lista proizvoda sa stanjem i količinama
proizvodi_1 = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2, "stanje": 5},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1, "stanje": 3}
]

proizvodi_2 = [
    {"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 5, "stanje": 0},  # Proizvod nije dostupan
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 3, "stanje": 10}
]

# Kreiranje i dodavanje narudžbi
napravi_narudzbu_s_uvjetima(proizvodi_1)  # Ova narudžba će biti uspješna
napravi_narudzbu_s_uvjetima(proizvodi_2)  # Ovdje će biti ispisana poruka da tipkovnica nije dostupna

# Ispis svih pohranjenih narudžbi
print("\nPohranjene narudžbe:")
for narudzba in narudzbe:
    print(narudzba.ispis_narudzbe())
