from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
destinos = {
"cartagena": 250000,
"medellin": 200000,
"san_andres": 300000
}

class Viaje(BaseModel):
    destino: str
personas: int
dias: int
@app.post("/cotizar")
def cotizar(viaje: Viaje):
    precio_base = destinos.get(viaje.destino.lower())
    if precio_base:
        total = precio_base * viaje.personas * viaje.dias
    return {"total": total}
    return {"error": "Destino no disponible"}