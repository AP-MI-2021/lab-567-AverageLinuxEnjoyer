from Domain.vanzare import getGen, getPret

def pretMinimGen(vanzari: list) -> dict:
    """Returneaza pretul minim pentru un gen

    Args:
        gen (str): Genul pentru care sa se determine pretul minim
        vanzari (list): [description]

    Returns:
        float: [description]
    """
    preturi_minime = dict()
    for vanzare in vanzari:
        if getGen(vanzare) not in preturi_minime or getPret(vanzare) < preturi_minime[getGen(vanzare)]:
            preturi_minime[getGen(vanzare)] = getPret(vanzare)

    return preturi_minime
    