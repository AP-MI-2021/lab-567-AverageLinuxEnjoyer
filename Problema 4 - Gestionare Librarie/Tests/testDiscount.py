from Domain.vanzare import getPret
from Logic.aplicareDiscount import aplicareDiscount
from Logic.CRUD import adaugareVanzare, getById


def testAplicareDiscount():
    vanzari = []
    vanzari = adaugareVanzare("1", "Fram, ursul polar", "Fictiune", 30.0, "silver", vanzari)
    vanzari = adaugareVanzare("2", "Harry Potter", "Fictiune", 35.0, "gold", vanzari)
    vanzari = adaugareVanzare("3", "Moara cu noroc", "Actiune", 13.99, "none", vanzari)

    aplicareDiscount(vanzari)

    assert getPret(getById("1", vanzari)) == 28.5
    assert getPret(getById("2", vanzari)) == 31.5
    assert getPret(getById("3", vanzari)) == 13.99


    