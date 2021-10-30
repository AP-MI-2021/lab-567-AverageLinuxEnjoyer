import datetime

class Expense:
    """Clasa folosita pentru reprezentarea unei cheltuieli

    Object Attributes:
        apartment_number (int): [Read Only] Numarul apartamentului corespunzator cheltuielii
        amount (int): Suma de bani
        expense_type (str): Tipul de cheltuiala
        date (str): Data la care a fost emisa o cheltuiala (DD.MM.YYYY)
    """

    def __init__(self, id: int, apartment_number: int, amount: int, expense_type: str, date: str = ""):
        """Initializeaza obiectul

        Args:
            apartment_number (int): Numarul apartamentului corespunzator cheltuielii
            amount (int): Suma de bani
            expense_type (str): Tipul de cheltuiala
            date (str, optional): Data la care a fost emisa o cheltuiala (DD.MM.YYYY). Daca nu e specificata va fi considerata data de azi.
        """
        self.__id = id
        self.__apartment_number = apartment_number
        self.__amount = amount
        self.__expense_type = expense_type
        self.__date = date

        if self.__date == "":
            self.__date = f"{datetime.datetime.today().date():%d.%m.%Y}"

    def __str__(self):
        return f"[Id: {self.__id}, "\
        f"Nr. apartament: {self.__apartment_number}, "\
        f"Suma: {self.__amount}, "\
        f"Tip de cheltuiala: {self.__expense_type}, "\
        f"Data: {self.__date}]"

    @property
    def id(self) -> int:
        """Getter id"""
        return self.__id
    
    @id.setter
    def id(self, new_id: int):
        raise RuntimeError("ID-ul este o modalitate de a identifica unic o cheltuiala, acesta nu trebuie modificat.")

    @property
    def apartment_number(self) -> int:
        """Getter apartment_number"""
        return self.__apartment_number

    @apartment_number.setter
    def apartment_number(self, new_apartment_number: int):
        """Setter apartment_number"""
        self.__apartment_number = new_apartment_number

    @property
    def amount(self) -> int:
        """Getter amount"""
        return self.__amount

    @amount.setter
    def amount(self, new_amount: int):
        """Setter amount"""
        self.__amount = new_amount

    @property
    def expense_type(self) -> str:
        """Getter expense_type"""
        return self.__expense_type

    @expense_type.setter
    def expense_type(self, new_expense_type: str):
        """Setter amount"""
        self.__expense_type = new_expense_type
        
    @property
    def date(self) -> str:
        """Getter date"""
        return self.__date

    @date.setter
    def date(self, new_date: str):
        """Setter date"""
        self.__date = new_date