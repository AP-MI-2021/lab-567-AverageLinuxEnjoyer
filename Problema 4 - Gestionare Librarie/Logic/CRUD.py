from Domain.vanzare import creeazaVanzare, getId

def adaugareVanzare(id: str, titlu: str, gen: str, pret: float, reducere: str, vanzari: list) -> list:
    """Adauga o vanzare noua in lista de vanzari

    Args:
        id (str): Id-ul vanzarii
        titlu (str): Titlul cartii vandute
        gen (str): Genul cartii vandute
        pret (float): Pretul cartii vandute
        reducere (str): Reducerea vanzarii
        vanzari (list): Lista de vanzari

    Returns:
        list: Lista de vanzari
    """
    vanzare_noua = creeazaVanzare(id, titlu, gen, pret, reducere)

    return vanzari + [vanzare_noua]

def stergereVanzare(id: str, vanzari: list) -> list:
    """Sterge vanzarea cu un anumit id din lista cu vanzari

    Args:
        id (str): Id-ul vanzarii sterse
        vanzari (list): Lista cu vanzari

    Returns:
        list: Noua lista cu vanzari
    """
    return [vanzare for vanzare in vanzari if getId(vanzare) != id]

def modificareVanzare(id: str, titlu: str, gen: str, pret: float, reducere: str, vanzari: list) -> list:
    """Modifica una din vanzarile din lista

    Args:
        id (str): Id-ul vanzarii care va fi modificata
        titlu (str): Noul titlu
        gen (str): Noul gen
        pret (float): Noul pret
        reducere (str): Noua reducere
        vanzari (list): Lista cu vanzari

    Returns:
        list: Lista cu vanzari
    """
    lista_noua = []

    for vanzare in vanzari:
        if getId(vanzare) == id:
            vanzare_noua = creeazaVanzare(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua            
    

def getById(id: str, vanzari: list) -> dict:
    """Returneaza vanzarea cu id-ul dat ca parametru

    Args:
        id (str): Id-ul vanzarii
        vanzari (lista): Lista de vanzari in care sa fie cautata vanzarea

    Returns:
        dict: Vanzarea cu id-ul dat ca parametru
    """
    for vanzare in vanzari:
        if getId(vanzare) == id:
            return vanzare

    return None