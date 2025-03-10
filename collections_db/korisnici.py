from fastapi import FastAPI
from typing import List
from models import Korisnik

app = FastAPI()

@app.post("/korisnik_registracija", response_model=List[Korisnik])
def registracija(korisnici:List[Korisnik]):
        return korisnici