import datetime
from enum import Enum

class ExpenseType(Enum):
    """Enum care se ocupa cu reprezentarea cheltuielilor.

    Tipuri de cheltuieli: 
        MAINTAINANCE - cheltuieli de intretinere
        SEWER - cheltuieli de canal
        OTHER_EXPENSES - alte cheltuieli
    """
    MAINTAINANCE = 1
    SEWER = 2
    OTHER_EXPENSES = 3


class Expense:
    """Clasa folosita pentru reprezentarea unei cheltuieli

    Object Attributes:
        apartment_number (int): Numarul apartamentului corespunzator cheltuielii
        amount (int): Suma de bani
        expense_type (ExpenseType): Tipul de cheltuiala
        date (datetime.date): Data la care a fost emisa o cheltuiala
    """

    def __init__(self, apartment_number: int, amount: int, expense_type: ExpenseType, date: datetime.date = None):
        """Initializeaza obiectul

        Args:
            apartment_number (int): Numarul apartamentului corespunzator cheltuielii
            amount (int): Suma de bani
            expense_type (ExpenseType): Tipul de cheltuiala
            date (datetime.date): Data la care a fost emisa o cheltuiala. Daca nu e specificata va fi considerata data de azi.
        """

        self.apartment_number = apartment_number
        self.amount = amount
        self.expense_type = expense_type
        self.date = date

        if self.date is None:
            self.date = datetime.datetime.today().date()

    @property
    def amount(self):
        """Getter amount"""
        return self.amount

    @amount.setter
    def amount(self, new_amount):
        """Setter amount"""
        return self.amount

    @property
    def expense_type(self):
        """Getter expense_type"""
        return self.expense_type