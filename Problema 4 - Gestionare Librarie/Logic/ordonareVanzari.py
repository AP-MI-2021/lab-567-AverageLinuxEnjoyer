from Domain.vanzare import getPret

def ordonareVanzari(vanzari: list) -> list:
    """Returneaza o lista cu vanzarile, ordonate crescator dupa pret

    Args:
        vanzari (list): Lista cu vanzarile

    Returns:
        list: Lista cu vanzarile, ordonata crescator
    """
    sorted_list = sorted(vanzari, key = lambda x: getPret(x))
    return sorted_list 