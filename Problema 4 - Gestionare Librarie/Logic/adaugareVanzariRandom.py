from Logic.CRUD import adaugareVanzare
from Domain.vanzare import getId
from random import randrange
from random import choice

def adaugareVanzariRandom(nr: int, vanzari: list) -> list:
    """Adauga un numar de vanzari random la lista de vanzari

    Args:
        nr (int): Numarul de vanzari adaugate
        vanzari (list): Lista de vanzari

    Returns:
        list: Noua lista
    """

    titluri_genuri = [
        ("Robinson Crusoe", "Actiune"),
        ("O calatorie spre centrul pamantului", "Actiune"),
        ("In linie dreapta", "Actiune"),
        ("Jocul de domino", "Mister"),
        ("Cazemata", "Mister"),
        ("Bani de hartie", "Mister"),
        ("Agentul Cormac", "Fantezie"),
        ("Razboiul elitelor", "Fantezie"),
        ("Golul temporal", "Fantezie"),
        ("Soarele umbrit", "Groaza"),
        ("Focul alb", "Groaza"),
        ("Taietura finala", "Groaza"),
        ("Soapte de iubire", "Romantism"),
        ("Genul ala de fata", "Romantism"),
        ("Camasa lui", "Romantism"),
        ("Orion va rasari", "Science Fiction"),
        ("Marginea fundatiei", "Science Fiction"),
        ("Existenta", "Science Fiction"),
        ("Alice in tara oglinzilor", "Nuvela"),
        ("Colt alb", "Nuvela"),
        ("Proza", "Nuvela"),
        ("Zogru", "Thriller"),
        ("Iubirea croitoresei", "Thriller"),
        ("Ultima iluzie", "Thriller")
    ]

    adaugate = []
    iduri_folosite = [getId(vanzare) for vanzare in vanzari]
    id_nou = 1

    for i in range(nr):
        while id_nou in iduri_folosite:
            id_nou += 1

        titlu_nou, gen_nou = titluri_genuri[randrange(len(titluri_genuri) - 1)]
        pret_nou = randrange(10, 250)
        reducere_noua = choice(["none", "silver", "gold"])

        adaugate = adaugareVanzare(str(id_nou), titlu_nou, gen_nou, pret_nou, reducere_noua, adaugate)

        iduri_folosite.append(id_nou)

    return vanzari + adaugate

