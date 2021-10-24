
def creeazaVanzare(id: int, titlu: str, gen: str, pret: int, reducere: str) -> dict:   
    """Creeaza si returneaza un dictionar ce reprezinta o vanzare

    Args:
        id (int): Id-ul dupa care va fi identificata vanzarea
        titlu (str): Titlul cartii vandute
        gen (str): Genul cartii vandute
        pret (int): Pretul cartii vandute
        reducere (str): Tipul de reducere (none, silver sau gold)

    Returns:
        dict: Dictionarul returnat
    """
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere
    }

def getId(vanzare: dict) -> int:
    """Returneaza id-ul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui id va fi returnat

    Returns:
        int: Id-ul returnat
    """
    return vanzare["id"]

def getTitlu(vanzare: dict) -> str:
    """Returneaza titlul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui titlu va fi returnat

    Returns:
        str: Titlul returnat
    """
    return vanzare["titlu"]

def getGen(vanzare: dict) -> str:
    """Returneaza genul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui gen va fi returnat

    Returns:
        str: Genul returnat
    """
    return vanzare["gen"]

def getPret(vanzare: dict) -> int:
    """Returneaza pretul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui pret va fi returnat

    Returns:
        int: Pretul returnat
    """
    return vanzare["pret"]

def getReducere(vanzare: dict) -> str:
    """Returneaza tipul de reducere al unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui tip de reducere va fi returnat

    Returns:
        str: Tipul de reducere returnat
    """
    return vanzare["reducere"]

def toString(vanzare: dict) -> str:
    """Returneaza dictionarul cu vanzarea convertit in string

    Args:
        vanzare (dict): Vanzarea ca dictionar

    Returns:
        str: Vanzarea ca string
    """
    return  f"Id: {getId(vanzare)}, Titlu: {getTitlu(vanzare)}, Gen: {getGen(vanzare)}, "\
            f"Pret: {getPret(vanzare)}, Reducere: {getReducere(vanzare)}"