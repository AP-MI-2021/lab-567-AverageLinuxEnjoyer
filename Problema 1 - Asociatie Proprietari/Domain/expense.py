import datetime
from enum import Enum


class ExpenseType(Enum):
    """Enum care se ocupa cu reprezentarea cheltuielilor.

    Tipuri de cheltuieli: 
        MAINTAINANCE - cheltuieli de intretinere
        SEWER - cheltuieli de canal
        OTHER - alte cheltuieli
    """
    MAINTAINANCE = "Cheltuieli de intretinere"
    SEWER = "Cheltuieli de canal"
    OTHER = "Alte cheltuieli"


class Expense:
    """Clasa folosita pentru reprezentarea unei cheltuieli

    Object Attributes:
        apartment_number (int): [Read Only] Numarul apartamentului corespunzator cheltuielii
        amount (int): Suma de bani
        expense_type (ExpenseType): Tipul de cheltuiala
        date (str): Data la care a fost emisa o cheltuiala (DD.MM.YYYY)
    """

    def __init__(self, apartment_number: int, amount: int, expense_type: ExpenseType, date: str = ""):
        """Initializeaza obiectul

        Args:
            apartment_number (int): Numarul apartamentului corespunzator cheltuielii
            amount (int): Suma de bani
            expense_type (ExpenseType): Tipul de cheltuiala
            date (str): Data la care a fost emisa o cheltuiala (DD.MM.YYYY). Daca nu e specificata va fi considerata data de azi.
        """
        
        self._apartment_number = apartment_number
        self._amount = amount
        self._expense_type = expense_type

        temp_date = [int(x) for x in date.split(".")]
        self._date = datetime.date(temp_date[2], temp_date[1], temp_date[0])

        if self._date == "":
            self._date = datetime.datetime.today().date()

    def __str__(self):
        return f"[Nr. apartament: {self._apartment_number}, "\
        f"Suma: {self._amount}, "\
        f"Tip de cheltuiala: {str(self._expense_type.value)}, "\
        f"Data: {self._date}]"

    @property
    def apartment_number(self) -> int:
        """Getter apartment_number"""
        return self._apartment_number

    @apartment_number.setter
    def apartment_number(self, new_apartment_number: int):
        raise RuntimeError("apartment_number setter called. The apartment_number acts as an ID, so it shouldn't be modified.")

    @property
    def amount(self) -> int:
        """Getter amount"""
        return self._amount

    @amount.setter
    def amount(self, new_amount: int):
        """Setter amount"""
        self._amount = new_amount

    @property
    def expense_type(self) -> ExpenseType:
        """Getter expense_type"""
        return self._expense_type

    @expense_type.setter
    def expense_type(self, new_expense_type: ExpenseType):
        """Setter amount"""
        self._expense_type = new_expense_type
        
    @property
    def date(self) -> datetime.date:
        """Getter date"""
        return self._date

    @date.setter
    def date(self, new_date: datetime.date):
        """Setter date"""
        print("date setter called")
        self._date = new_date


cheltuiala = Expense(1, 220, ExpenseType.MAINTAINANCE, "10.09.2019")

print(cheltuiala.apartment_number)
print(cheltuiala.amount)
print(cheltuiala.expense_type)
print(cheltuiala.date)

cheltuiala.amount = 200
cheltuiala.expense_type = ExpenseType.MAINTAINANCE
cheltuiala.date = datetime.date.today()

print(f"Cheltuiala: {cheltuiala}")