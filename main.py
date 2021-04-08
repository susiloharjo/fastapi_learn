from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    pengurangan = "kurang"
    penjumlahan = "jumlah"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{nama}")
async def hello(nama):
    return {"nama": nama}


@app.get("/jumlah/{satu}/{dua}")
def jumlah(satu: int, dua: int):
    return {"jumlah": (satu + dua)}


@app.get("/jumlah/{satu}/{dua}")
def kurang(satu: int, dua: int):
    return {"jumlah": (satu - dua)}


@app.get("/pilih/{metode}/{satu}/{dua}")
async def pilih(metode: ModelName, satu: int, dua: int):
    if metode.value == 'jumlah':
        print(metode.value)
        return jumlah(satu, dua)
    else:
        return kurang(satu, dua)
