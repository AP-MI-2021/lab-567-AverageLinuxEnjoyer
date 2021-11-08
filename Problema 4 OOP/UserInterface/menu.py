from Logic.sales_manager import SalesManager
from UserInterface.exceptionDecorator import valueErrorHandler

class Menu:
    accent_color = '\033[96m'
    normal_color = '\033[0m'
    
    def __init__(self, sales_manager: SalesManager):
        self.__sales_manager = sales_manager
    
    def run(self):
        option = " "
        
        while True:
            self.printMenu()
            option = input("Optiune: ")

            if option == "0":
                self.addSaleMenu()
            elif option == "1":
                self.removeSaleMenu()
            elif option == "2":
                self.modifySaleMenu()
            elif option == "3":
                self.__sales_manager.applyDiscounts()
                print("Discount-uri aplicate.")
            elif option == "4":
                self.modifyGenreToAllTitlesMenu()
            elif option == "5":
                self.getMinimumPricePerGenreMenu()
            elif option == "6":
                self.__sales_manager.orderSalesByPrice()
                self.showAll()
            elif option == "7":
                self.getDistinctTitlesPerGenre()
            
            elif option == "8":
                self.__sales_manager.undo()
            elif option == "9":
                self.__sales_manager.redo()
            
            elif option == "a":
                self.showAll()
            elif option == "r":
                self.addRandomSalesMenu()
            elif option == "x":
                break
    
    @valueErrorHandler
    def addSaleMenu(self):
        id = int(input("Id vanzare: "))
        title = input("Titlul cartii: ")
        genre = input("Genul cartii: ")
        price = float(input("Pretul cartii: "))
        discount_type = input("Tipul de reducere (none, silver, gold): ")
        
        self.__sales_manager.addSale(id, title, genre, price, discount_type)
    
    @valueErrorHandler
    def removeSaleMenu(self):
        id = int(input("Id vanzare: "))
        
        self.__sales_manager.removeSale(id)
    
    @valueErrorHandler
    def modifySaleMenu(self):
        id = int(input("Id vanzare: "))
        title = input("Noul titlu al cartii: ")
        genre = input("Noul gen al cartii: ")
        price = float(input("Noul pret al cartii: "))
        discount_type = input("Noul tip de reducere (none, silver, gold): ")
        
        self.__sales_manager.modifySale(id, title, genre, price, discount_type)        
    
    def modifyGenreToAllTitlesMenu(self):
        title = input("Titlul cartii al carui gen trebuie modificat: ")
        genre = input("Noul gen al cartii: ")
        
        self.__sales_manager.modifyGenreToAllTitles(title, genre)
        
        print("Genul cartilor modificat cu succes!")
    
    def getMinimumPricePerGenreMenu(self):
        c = Menu.accent_color
        n = Menu.normal_color
        
        dictionary = self.__sales_manager.getMinimumPricePerGenre()
        
        for genre, price in dictionary.items():
            print(f"{c + genre + ':' + n:<30} {price}")
    
    def getDistinctTitlesPerGenre(self):
        c = Menu.accent_color
        n = Menu.normal_color
        
        pairs_list = self.__sales_manager.getDistinctTitlesPerGenre()
        
        for genre, titles_num in pairs_list:
            print(f"{c + genre + ':' + n:<30} {titles_num}")
    
    def showAll(self):
        sales = self.__sales_manager.sales
        
        for sale in sales:
            print(sale)
            
    def addRandomSalesMenu(self):
        count = int(input("Cate vanzari random sa fie adaugate? "))
        self.__sales_manager.addRandomSales(count)
        
        if count <= 0:
            print("Nu a fost adaugata nici o vanzare random.")
        elif count == 1:
            print("A fost adaugata o vanzare random.")
        elif count >= 2:
            print(f"Au fost adaugate {count} vanzari random.")
    
    def printMenu(self):
        c = Menu.accent_color
        n = Menu.normal_color

        print(f"""
    {c}(0){n}  Adaugare vanzare.
    {c}(1){n}  Stergere vanzare.
    {c}(2){n}  Modificare vanzare.
    {c}(3){n}  Aplicare discount tuturor vanzarilor. (5% pentru silver, 10% pentru gold)
    {c}(4){n}  Modificarea genului pentru un titlu dat.
    {c}(5){n}  Determinarea pretului minim pentru fiecare gen.
    {c}(6){n}  Ordonarea crescatoare a vanzarilor, dupa pret.
    {c}(7){n}  Afisarea numarului de titluri distincte pentru fiecare gen.

    {c}(8){n}  Undo
    {c}(9){n}  Redo

    {c}(a){n}  Afisarea tututor vanzarilor
    {c}(r){n}  Adaugare vanzari random la lista. (ca sa va usurez viata)
    {c}(x){n}  Iesire 
    """)