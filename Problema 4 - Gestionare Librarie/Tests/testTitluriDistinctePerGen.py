from Logic.titluriDistincte import titluriDistinctePerGen
from Logic.CRUD import adaugareVanzare

def testTitluriDistinctePerGen():
    vanzari = []

    vanzari = adaugareVanzare("1", "Ion", "Realist", 20.0, "none", vanzari)
    vanzari = adaugareVanzare("7", "Ion", "Realist", 20.0, "none", vanzari)
    vanzari = adaugareVanzare("2", "Moara cu noroc", "Realist", 70.0, "none", vanzari)
    vanzari = adaugareVanzare("3", "Enigma Otiliei", "Psihologie", 15.0, "none", vanzari)
    vanzari = adaugareVanzare("8", "Enigma Otiliei", "Psihologie", 15.0, "none", vanzari)
    vanzari = adaugareVanzare("9", "Enigma Otiliei", "Psihologie", 15.0, "none", vanzari)
    vanzari = adaugareVanzare("4", "Alexandru Lapusneanu", "Realist", 25.99, "none", vanzari)
    vanzari = adaugareVanzare("5", "Ultima noapte", "Psihologie", 64.0, "none", vanzari)
    vanzari = adaugareVanzare("10", "Ultima noapte", "Psihologie", 64.0, "none", vanzari)
    vanzari = adaugareVanzare("6", "Harap Alb", "Fantastic", 120.0, "none", vanzari)
    vanzari = adaugareVanzare("11", "Harap Alb", "Fantastic", 120.0, "none", vanzari)

    assert titluriDistinctePerGen(vanzari) == [('Realist', 3), ('Psihologie', 2), ('Fantastic', 1)]
