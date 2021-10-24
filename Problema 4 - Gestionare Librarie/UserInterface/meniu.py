from UserInterface.meniuCRUD import meniuAdaugareVanzare, meniuStergereVanzare, meniuModificareVanzare
from Domain.vanzare import toString
from Logic.aplicareDiscount import aplicareDiscount
from Logic.modificareGen import modificareGen

def afisareaTututorVanzarilor(vanzari: list):
    for vanzare in vanzari:
        print(toString(vanzare))

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
            pass
        elif optiune == "7":
            pass
        elif optiune == "8":
            pass
        elif optiune == "9":
            pass
        elif optiune == "a":
            afisareaTututorVanzarilor(vanzari)
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
    (x) Iesire 
    """)