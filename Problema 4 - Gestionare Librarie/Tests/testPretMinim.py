from Logic.pretMinim import pretMinimGen
from Logic.CRUD import adaugareVanzare

def testPretMinimGen():
    vanzari = []

    vanzari = adaugareVanzare("1", "Ion", "Realist", 20.0, "none", vanzari)
    vanzari = adaugareVanzare("2", "Moara cu noroc", "Realist", 70.0, "none", vanzari)
    vanzari = adaugareVanzare("3", "Enigma Otiliei", "Psihologie", 15.0, "none", vanzari)
    vanzari = adaugareVanzare("4", "Alexandru Lapusneanu", "Realist", 25.99, "none", vanzari)
    vanzari = adaugareVanzare("5", "Ultima noapte", "Psihologie", 64.0, "none", vanzari)
    vanzari = adaugareVanzare("6", "Harap Alb", "Fantastic", 120.0, "none", vanzari)

    assert pretMinimGen(vanzari) == {"Realist":20.0, "Psihologie":15.0, "Fantastic": 120}