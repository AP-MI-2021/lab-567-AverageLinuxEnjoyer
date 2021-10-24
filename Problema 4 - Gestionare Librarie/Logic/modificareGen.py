from Domain.vanzare import setGen, getTitlu
from Logic.CRUD import getById

def modificareGen(titlu: str, gen_nou: str, vanzari: list):
    """Modifica genul unei vanzari, gasita dupa titlul cartii

    Args:
        titlu (str): Titlul cartii al carui gen e modificat
        gen_nou (str): Noul gen al cartii
        vanzari (list): Lista de vanzari in care sunt gasite toate titlurile
    """
    for vanzare in vanzari:
        if getTitlu(vanzare) == titlu:
            setGen(vanzare, gen_nou)