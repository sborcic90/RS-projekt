from pydantic import BaseModel

class Korisnik(BaseModel):
    ime: str
    prezime: str
    email: str
    username: str
    lozinka: str