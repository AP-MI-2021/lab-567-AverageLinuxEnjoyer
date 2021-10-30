from Logic.owners_association import OwnersAssociation

class Menu:
    def __init__(self, owners_association: OwnersAssociation):
        """Initializeaza obiectul"""
        self.__owners_association = owners_association
        
        
    def display_main_menu(self):
        """Afiseaza meniul principal
        """

        print("""
        0. Adaugare cheltuiala.
        1. Stergere cheltuiala.
        2. Modificare cheltuiala.
        3. Stergerea tuturor cheltuielilor unui apartament.
        4. Adunarea unei valori la toate cheltuielile dintr-o data citita.
        5. Determinarea celei mai mari cheltuieli de un anumit tip.
        6. Ordonarea cheltuielilor descrescator dupa suma.
        7. Afisarea sumelor lunare pentru fiecare apartament.
        8. Undo
        9. Redo
        a. Afisarea tuturor cheltuielilor
        x. Iesire
        """)

    def addExpense(self):
        """Meniu pentru adaugarea unei cheltuieli
        """
        id = int(input("Id: "))
        apartment_number = int(input("Numar apartament: "))
        amount = int(input("Suma: "))
        expense_type = input("Tipul (intretinere / canal / alte cheltuieli):")
        date = input("Data (DD.MM.YYYY): ")
        
        self.__owners_association.addExpense(id, apartment_number, amount, expense_type, date)
        
    def removeExpense(self):
        """Meniu pentru stergerea unei cheltuieli
        """
        id = int(input("Id: "))
        
        self.__owners_association.removeExpense(id)
     
    def modifyExpense(self):
        """Meniu pentru modificarea unei cheltuieli
        """
        id = int(input("ID-ul cheltuielii modificate: "))
        
        apartment_number = int(input("Numar apartament: "))
        amount = int(input("Suma: "))
        expense_type = input("Tipul (intretinere / canal / alte cheltuieli):")
        date = input("Data (DD.MM.YYYY): ")
        
        self.__owners_association.modifyExpense(id, apartment_number, amount, expense_type, date)
        
     
    def showAllExpenses(self):
        """Afiseaza toate cheltuielile
        """
        for expense in self.__owners_association.getAllExpenses():
            print(str(expense))
        
    def run_menu(self):
        """Main loop-ul principal cu intregul meniu
        """
        
        option = ""
        
        while True:
            self.display_main_menu()
            
            option = input("Optiune:")
            
            if option == "0":
                self.addExpense()
            elif option == "1":
                self.removeExpense()
            elif option == "2":
                self.modifyExpense()
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                pass
            elif option == "6":
                pass
            elif option == "7":
                pass
            
            elif option == "8":
                pass
            elif option == "9":
                pass
            
            elif option == "a":
                self.showAllExpenses()
            elif option == "x":
                break