from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare, getById
from Domain.vanzare import creeazaVanzare, getId, getTitlu, getGen, getPret, getReducere, toString

def testCRUD():
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()

def testAdaugareVanzare():
    vanzari = []
    vanzari = adaugareVanzare("1", "Fram, ursul polar", "Fictiune", 27.99, "silver", vanzari)
    
    assert getId(getById("1", vanzari)) == "1"
    assert getTitlu(getById("1", vanzari)) == "Fram, ursul polar"
    assert getGen(getById("1", vanzari)) == "Fictiune"
    assert getPret(getById("1", vanzari)) == 27.99
    assert getReducere(getById("1", vanzari)) == "silver"

def testStergereVanzare():
    vanzari = []
    vanzari = adaugareVanzare("1", "Fram, ursul polar", "Fictiune", 27.99, "silver", vanzari)
    vanzari = adaugareVanzare("2", "Harry Potter", "Fictiune", 35.49, "gold", vanzari)

    vanzari = stergereVanzare("1", vanzari)

    assert getById("1", vanzari) is None
    assert getById("2", vanzari) is not None   
    assert len(vanzari) == 1

    vanzari = stergereVanzare("4", vanzari)

    assert getById("2", vanzari) is not None
    assert len(vanzari) == 1

    vanzari = stergereVanzare("2", vanzari)

    assert getById("2", vanzari) is None
    assert len(vanzari) == 0

def testModificareVanzare():
    vanzari = []
    vanzari = adaugareVanzare("2", "Harry Potter", "Fictiune", 35.49, "gold", vanzari)

    vanzari = modificareVanzare("2", "Harry Potter and the Chamber of Secrets", "Fictiune", 40.0, "silver", vanzari)

    assert getTitlu(getById("2", vanzari)) == "Harry Potter and the Chamber of Secrets"
    assert getGen(getById("2", vanzari)) == "Fictiune"
    assert getPret(getById("2", vanzari)) == 40.0
    assert getReducere(getById("2", vanzari)) == "silver"

