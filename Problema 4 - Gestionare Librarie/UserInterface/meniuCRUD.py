from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare
from UserInterface.exceptionDecorator import valueErrorHandler

@valueErrorHandler
def meniuAdaugareVanzare(vanzari: list):
    
    id = input("Id vanzare: ")
    titlu = input("Titlul cartii: ")
    gen = input("Genul cartii: ")
    pret = float(input("Pretul cartii: "))
    reducere = input("Tipul de reducere (none, silver, gold): ")

    return adaugareVanzare(id, titlu, gen, pret, reducere, vanzari)


def meniuStergereVanzare(vanzari: list):
    id = input("Id vanzare stearsa: ")

    return stergereVanzare(id, vanzari)

@valueErrorHandler
def meniuModificareVanzare(vanzari: list):
    
    id = input("Id-ul vanzarii ce va fi modificata: ")
    titlu = input("Noul titlu al cartii: ")
    gen = input("Noul gen al cartii: ")
    pret = float(input("Noul pret al cartii: "))
    reducere = input("Noul tip de reducere (none, silver, gold): ")
    return modificareVanzare(id, titlu, gen, pret, reducere, vanzari)

    return vanzari