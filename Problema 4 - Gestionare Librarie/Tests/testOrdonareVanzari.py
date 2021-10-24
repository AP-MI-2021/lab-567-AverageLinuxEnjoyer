from Logic.ordonareVanzari import ordonareVanzari
from Logic.CRUD import adaugareVanzare
from Domain.vanzare import getPret

def testOrdonareVanzari():
    vanzari = []

    vanzari = adaugareVanzare("1", "Ion", "Realist", 20.0, "none", vanzari)
    vanzari = adaugareVanzare("2", "Moara cu noroc", "Realist", 70.0, "none", vanzari)
    vanzari = adaugareVanzare("3", "Enigma Otiliei", "Psihologie", 15.0, "none", vanzari)
    vanzari = adaugareVanzare("4", "Alexandru Lapusneanu", "Realist", 25.99, "none", vanzari)
    vanzari = adaugareVanzare("5", "Ultima noapte", "Psihologie", 64.0, "none", vanzari)
    vanzari = adaugareVanzare("6", "Harap Alb", "Fantastic", 120.0, "none", vanzari)

    vanzari = ordonareVanzari(vanzari)

    assert [getPret(vanzare) for vanzare in vanzari] == [15.0, 20.0, 25.99, 64.0, 70.0, 120.0]