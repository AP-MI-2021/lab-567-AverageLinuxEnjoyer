from UserInterface.meniuCRUD import meniuAdaugareVanzare, meniuStergereVanzare, meniuModificareVanzare
from Domain.vanzare import toString
from Logic.aplicareDiscount import aplicareDiscount
from Logic.modificareGen import modificareGen
from Logic.pretMinim import pretMinimGen
from Logic.ordonareVanzari import ordonareVanzari
from Logic.titluriDistincte import titluriDistinctePerGen
from Logic.adaugareVanzariRandom import adaugareVanzariRandom

def afisareaTututorVanzarilor(vanzari: list):
    for vanzare in vanzari:
        print(toString(vanzare))

def afisarePretMinimPeGen(vanzari: list):
    preturi = pretMinimGen(vanzari)
    for gen, pret in preturi.items():
        print(f"Cel mai mic pret pentru genul {gen} este {pret}.")

def afisareTitluriDistinctePerGen(vanzari: list):
    perechi = titluriDistinctePerGen(vanzari)
    for gen, nr_titluri in perechi:
        print(f"{gen}: {nr_titluri}")

def meniuAdaugareVanzariRandom(vanzari: list) -> list:
    nr = int(input("Cate vanzari random sa fie adaugate? "))
    return adaugareVanzariRandom(nr, vanzari)


def meniuModificareGen(vanzari: list):
    titlu = input("Carei carti ii va fi schimbat genul? ")
    gen_nou = input("Care este noul gen? ")
    modificareGen(titlu, gen_nou, vanzari)

def runMenu(vanzari: list):
    while True:
        printMeniu()
        optiune = input("Optiune: ")

        if optiune == "1":
            vanzari = meniuAdaugareVanzare(vanzari)
        elif optiune == "2":
            vanzari = meniuStergereVanzare(vanzari)
        elif optiune == "3":
            vanzari = meniuModificareVanzare(vanzari)
        elif optiune == "4":
            aplicareDiscount(vanzari)
        elif optiune == "5":
            meniuModificareGen(vanzari)
        elif optiune == "6":
            afisarePretMinimPeGen(vanzari)
        elif optiune == "7":
            vanzari = ordonareVanzari(vanzari)
        elif optiune == "8":
            vanzari = afisareTitluriDistinctePerGen(vanzari)
        elif optiune == "9":
            pass
        elif optiune == "a":
            afisareaTututorVanzarilor(vanzari)
        elif optiune == "r":
            vanzari = meniuAdaugareVanzariRandom(vanzari)
        elif optiune == "x":
            break        

def printMeniu():
    print("""
    (1) Adaugare vanzare.
    (2) Stergere vanzare.
    (3) Modificare vanzare.
    (4) Aplicare discount tuturor vanzarilor. (5% pentru silver, 10% pentru gold)
    (5) Modificarea genului pentru un titlu dat.
    (6) Determinarea pretului minim pentru fiecare gen.
    (7) Ordonarea crescatoare a vanzarilor, dupa pret.
    (8) Afisarea numarului de titluri distincte pentru fiecare gen.
    (9) Undo
    (a) Afisarea tututor vanzarilor
    (r) Adaugare vanzari random la lista. (ca sa va usurez viata)
    (x) Iesire 
    """)