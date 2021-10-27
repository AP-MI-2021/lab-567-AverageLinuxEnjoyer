from UserInterface.meniuCRUD import meniuAdaugareVanzare, meniuStergereVanzare, meniuModificareVanzare
from UserInterface.colors import Colors
from Domain.vanzare import toString
from Logic.aplicareDiscount import aplicareDiscount
from Logic.modificareGen import modificareGen
from Logic.pretMinim import pretMinimGen
from Logic.ordonareVanzari import ordonareVanzari
from Logic.titluriDistincte import titluriDistinctePerGen
from Logic.adaugareVanzariRandom import adaugareVanzariRandom
import copy


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

    states = [[]]
    vanzari = []
    index = 0

    while True:
        printMeniu()
        optiune = input("Optiune: ")

        if optiune == "0":
            vanzari = meniuAdaugareVanzare(vanzari)
        elif optiune == "1":
            vanzari = meniuStergereVanzare(vanzari)
        elif optiune == "2":
            vanzari = meniuModificareVanzare(vanzari)
        elif optiune == "3":
            vanzari = aplicareDiscount(vanzari)
        elif optiune == "4":
            meniuModificareGen(vanzari)
        elif optiune == "5":
            afisarePretMinimPeGen(vanzari)
        elif optiune == "6":
            vanzari = ordonareVanzari(vanzari)
        elif optiune == "7":
            afisareTitluriDistinctePerGen(vanzari)

        elif optiune == "8":  # Undo
            if index > 0:
                index -= 1
            vanzari = states[index]
        elif optiune == "9": # Redo
            if index < len(states) - 1:
                index += 1
            vanzari = states[index]
                
        elif optiune == "a":
            afisareaTututorVanzarilor(vanzari)
        elif optiune == "r":
            vanzari = meniuAdaugareVanzariRandom(vanzari)
        elif optiune == "x":
            break
        
        if optiune in ["1","2","3","4","5", "7","r"]:
            states = states[:index+1]
            states.append(copy.deepcopy(vanzari))
            index = len(states) - 1
            vanzari = states[-1]
                

def printMeniu():
    c = Colors.OKCYAN
    e = Colors.ENDC

    print(f"""
    {c}(0){e}  Adaugare vanzare.
    {c}(1){e}  Stergere vanzare.
    {c}(2){e}  Modificare vanzare.
    {c}(3){e}  Aplicare discount tuturor vanzarilor. (5% pentru silver, 10% pentru gold)
    {c}(4){e}  Modificarea genului pentru un titlu dat.
    {c}(5){e}  Determinarea pretului minim pentru fiecare gen.
    {c}(6){e}  Ordonarea crescatoare a vanzarilor, dupa pret.
    {c}(7){e}  Afisarea numarului de titluri distincte pentru fiecare gen.

    {c}(8){e}  Undo
    {c}(9){e}  Redo

    {c}(a){e}  Afisarea tututor vanzarilor
    {c}(r){e}  Adaugare vanzari random la lista. (ca sa va usurez viata)
    {c}(x){e}  Iesire 
    """)