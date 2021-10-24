from Domain.vanzare import getGen, getTitlu


def titluriDistinctePerGen(vanzari: list) -> list:
    """Returneaza numarul de titluri distincte pentru fiecare gen

    Args:
        vanzari (list): Lista cu vanzarile

    Returns:
        list: O lista cu perechi (gen, numar de titluri distincte)
    """
    titluri_distincte = dict()

    for vanzare in vanzari:
        if getGen(vanzare) not in titluri_distincte:
            titluri_distincte[getGen(vanzare)] = {getTitlu(vanzare)}
        else:
            titluri_distincte[getGen(vanzare)].add(getTitlu(vanzare))

    return [(gen, len(titluri)) for gen, titluri in titluri_distincte.items()]
