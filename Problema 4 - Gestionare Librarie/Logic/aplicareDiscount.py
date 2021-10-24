from Domain.vanzare import getReducere, getPret, setPret

def aplicareDiscount(vanzari: list) -> list:
    """Aplica un discount de 5% si 10% pentru vanzarile de tip silver, respectiv gold

    Args:
        vanzari (list): Lista de vanzari initiala

    Returns:
        list: Lista de vanzari dupa aplicarea discount-urilor
    """
    lista_noua = []

    for vanzare in vanzari:
        if getReducere(vanzare) == "silver":
            pret_nou = getPret(vanzare) * 0.95
        elif getReducere(vanzare) == "gold":
            pret_nou = getPret(vanzare) * 0.9
        else:
            pret_nou = getPret(vanzare)

        setPret(vanzare, pret_nou)