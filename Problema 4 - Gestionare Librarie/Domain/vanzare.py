
def creeazaVanzare(id: str, titlu: str, gen: str, pret: float, reducere: str) -> dict:   
    """Creeaza si returneaza un dictionar ce reprezinta o vanzare

    Args:
        id (str): Id-ul dupa care va fi identificata vanzarea
        titlu (str): Titlul cartii vandute
        gen (str): Genul cartii vandute
        pret (float): Pretul cartii vandute
        reducere (str): Tipul de reducere (none, silver sau gold)

    Returns:
        dict: Dictionarul returnat
    """
    return [id,titlu, gen, pret, reducere]

def getId(vanzare: dict) -> str:
    """Returneaza id-ul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui id va fi returnat

    Returns:
        str: Id-ul returnat
    """
    return vanzare[0]

def getTitlu(vanzare: dict) -> str:
    """Returneaza titlul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui titlu va fi returnat

    Returns:
        str: Titlul returnat
    """
    return vanzare[1]

def getGen(vanzare: dict) -> str:
    """Returneaza genul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui gen va fi returnat

    Returns:
        str: Genul returnat
    """
    return vanzare[2]

def setGen(vanzare: dict, gen_nou: str):
    """Modifica genul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui gen e modificat
        gen_nou (str): Noul gen
    """
    vanzare[2] = gen_nou

def getPret(vanzare: dict) -> float:
    """Returneaza pretul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui pret va fi returnat

    Returns:
        float: Pretul returnat
    """
    return vanzare[3]

def setPret(vanzare: dict, pret_nou: float):
    """Modifica pretul unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui pret e modificat
        pret_nou (float): Noul pret
    """
    vanzare[3] = pret_nou

def getReducere(vanzare: dict) -> str:
    """Returneaza tipul de reducere al unei vanzari

    Args:
        vanzare (dict): Vanzarea al carui tip de reducere va fi returnat

    Returns:
        str: Tipul de reducere returnat
    """
    return vanzare[4]

def toString(vanzare: dict) -> str:
    """Returneaza dictionarul cu vanzarea convertit in string

    Args:
        vanzare (dict): Vanzarea ca dictionar

    Returns:
        str: Vanzarea ca string
    """
    return  f"{'Id: ' + getId(vanzare):<10} {'Titlu: ' + getTitlu(vanzare):<45} {'Gen: ' + getGen(vanzare):<23}"\
            f"{'Pret: ' + str(round(getPret(vanzare), 2)):<13} Reducere: {getReducere(vanzare)}"


