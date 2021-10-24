from Logic.modificareGen import modificareGen
from Logic.CRUD import adaugareVanzare, getById
from Domain.vanzare import getGen

def testModificareGen():
    vanzari = []
    vanzari = adaugareVanzare("1", "Fram, ursul polar", "Fictiune", 30.0, "silver", vanzari)
    vanzari = adaugareVanzare("2", "Harry Potter", "Fictiune", 35.0, "gold", vanzari)
    vanzari = adaugareVanzare("3", "Moara cu noroc", "Actiune", 13.99, "none", vanzari)

    modificareGen("Moara cu noroc", "Psihologie", vanzari)
    assert getGen(getById("3", vanzari)) == "Psihologie"

    modificareGen("Harry Potter", "Drama", vanzari)
    assert getGen(getById("2", vanzari)) == "Drama"

    modificareGen("Fram, ursul polar", "Fictiune", vanzari)
    assert getGen(getById("1", vanzari)) == "Fictiune"
