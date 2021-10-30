from Domain.expense import Expense

class OwnersAssociation:
    def __init__(self):
        """Initializeaza obiectul"""
        self.__expenses: list[Expense] = []
    
    def addExpense(self, id: int, apartment_number: int, amount: int, expense_type: str, date: str = ""):
        """Adauga o cheltuiala

        Args:
            id (int): Id-ul cheltuielii
            apartment_number (int): Numarul apartamentului
            amount (int): Suma de bani
            expense_type (str): Tipul de cheltuiala
            date (str, optional): Data la care a fost emisa o cheltuiala (DD.MM.YYYY). Daca nu e specificata va fi considerata data de azi.
        """
        
        self.__expenses.append(Expense(id, apartment_number, amount, expense_type, date))
        
    def removeExpense(self, id: int):
        """Sterge o cheltuiala

        Args:
            id (int): ID-ul cheltuielii care trebuie stearsa.
        """
        for i in range(len(self.__expenses)):
            current_expense = self.__expenses[i]
            if current_expense.id == id:
                self.__expenses.remove(current_expense)
                break
            
    def modifyExpense(self, id: int, apartment_number: int, amount: int, expense_type: str, date: str = ""):
        """Modifica o cheltuialall

        Args:
            id (int): Id-ul cheltuielii
            apartment_number (int): Numarul apartamentului
            amount (int): Suma de bani
            expense_type (ExpenseType): Tipul de cheltuiala
            date (str, optional): Data la care a fost emisa o cheltuiala (DD.MM.YYYY). Daca nu e specificata va fi considerata data de azi.
        """
        expense = self.getExpense(id)
        expense.apartment_number    = apartment_number
        expense.amount              = amount
        expense.expense_type        = expense_type
        expense.date                = date
        
    def getExpense(self, id: int) -> Expense:
        """Returneaza cheltuiala cu id-ul dat

        Args:
            id (int): numarul dupa care se identifica cheltuiala

        Returns:
            Expense: cheltuiala cu id-ul dat, in caz contrar se returneaza None 
        """
        for expense in self.__expenses:
            if expense.id == id:
                return expense
            
        return None
    
    def getAllExpenses(self) -> list[Expense]:
        """Returneaza o lista cu toate cheltuielile

        Returns:
            list[Expense]: Lista cu toate cheltuielile
        """
        return self.__expenses
        
    