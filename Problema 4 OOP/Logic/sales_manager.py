from Domain.sale import Sale
from random import randrange
from random import choice
from copy import deepcopy

class SalesManager:
    def __init__(self):
        """Constructorul unui obiect de tip SalesManager
        """
        self.__sales = []
        self.__undo_operations = []
        self.__redo_operations = []
        
    @property
    def sales(self):
        """Getter lista vanzari"""
        return self.__sales
        
    def getByID(self, id: int):
        """Returneaza vanzarea cu un anumit id

        Args:
            id (int): id-ul vanzarii
        """
        for sale in self.__sales:
            if sale.id == id:
                return sale
            
        return None
        
    def undo(self):
        """Operatia de undo"""
        if len(self.__undo_operations) > 0:
            operations = self.__undo_operations.pop()
            self.__redo_operations.append(operations)
            operations[0]()
            
    def redo(self):
        """Operatia de redo"""
        if len(self.__redo_operations) > 0:
            operations = self.__redo_operations.pop()
            self.__undo_operations.append(operations)
            operations[1]()
    
    def addSale(self, id: int, title: str, genre: str, price: float, discount_type: str) -> None:
        """Adauga o vanzare in lista vanzarilor

        Args:
            id (int): ID-ul vanzarii
            title (str): Titlul cartii vandute
            genre (str): Genul cartii vandute
            price (float): Pretul cartii
            discount_type (str): Tipul de discount (none/silver/gold)
        """
        self.__sales.append(Sale(id, title, genre, price, discount_type))
        
        def remove():
            self.__sales = [sale for sale in self.__sales if sale.id != id]
        
        def add():
            self.__sales.append(Sale(id, title, genre, price, discount_type))
        
        self.__undo_operations.append([
            lambda: remove(), 
            lambda: add()
        ])
        
        self.__redo_operations.clear()
        
    def removeSale(self, id: int) -> None:
        """Sterge o vanzare din lista vanzarilor

        Args:
            id (int): ID-ul vanzarii sterse
        """
        deleted_sale = self.getByID(id)
        
        self.__sales = [sale for sale in self.__sales if sale.id != id]
        
        def add():
            self.__sales.append(deleted_sale)
            
        def remove():
            self.__sales = [sale for sale in self.__sales if sale.id != id]
            
        self.__undo_operations.append([
            lambda: add(),
            lambda: remove()
        ])
        
        self.__redo_operations.clear()
        
    def modifySale(self, id: int, title: str, genre: str, price: float, discount_type: str) -> None:
        """Modifica o vanzare in lista vanzarilor

        Args:
            id (int): ID-ul vanzarii
            title (str): Titlul cartii vandute
            genre (str): Genul cartii vandute
            price (float): Pretul cartii
            discount_type (str): Tipul de discount (none/silver/gold)
        """
        index = -1
        
        for i in range(len(self.__sales)):
            if self.__sales[i].id == id:
                index = i
                old_sale = self.__sales[i]
                self.__sales[i] = Sale(id, title, genre, price, discount_type)
        
        def revertSaleChange():
            self.__sales[index] = old_sale

        def modify():
            self.__sales[index] = Sale(id, title, genre, price, discount_type)

        self.__undo_operations.append([
            lambda: revertSaleChange(),
            lambda: modify()
        ])

        self.__redo_operations.clear()       
                
    def applyDiscounts(self) -> None:
        """Aplica un discount de 5%,10% pentru vanzarile de tip silver, respectiv gold"""
        
        for sale in self.__sales:
            if sale.discount_type == "silver":
                sale.price = sale.price * 0.95
            elif sale.discount_type == "gold":
                sale.price = sale.price * 0.9
        
        def revertDiscounts(): 
            for sale in self.__sales:
                if sale.discount_type == "silver":
                    sale.price = sale.price * (20 / 19)
                elif sale.discount_type == "gold":
                    sale.price = sale.price * (10 / 9)
                
        def reapplyDiscounts():
            for sale in self.__sales:
                if sale.discount_type == "silver":
                    sale.price = sale.price * 0.95
                elif sale.discount_type == "gold":
                    sale.price = sale.price * 0.9
                
        self.__undo_operations.append([
            lambda: revertDiscounts(),
            lambda: reapplyDiscounts()
        ])
        
        self.__redo_operations.clear()
        
    def modifyGenreToAllTitles(self, title: str, new_genre: str) -> None:
        """Modifica genul tuturor vanzarilor cu un anumit titlu

        Args:
            title (str): Titlul dat
            new_genre (str): Noul gen
        """
        old_sales = deepcopy(self.__sales)
        
        for sale in self.__sales:
            if sale.title == title:
                sale.genre = new_genre
           
        def revertGenreChange():
            self.__sales = old_sales
                
        def reapplyGenreChange():
            for sale in self.__sales:
                if sale.title == title:
                    sale.genre = new_genre
                
        self.__undo_operations.append([
            lambda: revertGenreChange(),
            lambda: reapplyGenreChange()
        ])
        
        self.__redo_operations.clear()
    
    def getMinimumPricePerGenre(self) -> dict:
        """Returneaza un dictionar care contine genurile si pretul cel mai mic pentru fiecare gen

        Returns:
            dict: Dictionarul returnat
        """
        
        minimum_prices = dict()
        for sale in self.__sales:
            if sale.genre not in minimum_prices or sale.price < minimum_prices[sale.genre]:
                minimum_prices[sale.genre] = sale.price

        return minimum_prices
    
    def orderSalesByPrice(self) -> None:
        """Ordoneaza vanzarile crescator dupa pret"""
        
        sales_before_sorting = deepcopy(self.__sales)
        self.__sales = sorted(self.__sales, key = lambda x: x.price)
        
        def revertSorting():
            self.__sales = sales_before_sorting
        
        def reapplySorting():
            self.__sales = sorted(self.__sales, key = lambda x: x.price)
        
        self.__undo_operations.append([
            lambda: revertSorting(),
            lambda: reapplySorting()
        ])
        
        self.__redo_operations.clear()
        
    def getDistinctTitlesPerGenre(self) -> list:
        """Returneaza numarul de titluri distincte pentru fiecare gen
        
        Returns:
            list: O lista cu perechi (gen, numar de titluri distincte)
        """
        distinct_titles = dict()

        for sale in self.__sales:
            if sale.genre not in distinct_titles:
                distinct_titles[sale.genre] = {sale.title}
            else:
                distinct_titles[sale.genre].add(sale.title)

        return [(genre, len(title)) for genre, title in distinct_titles.items()]

    
    def addRandomSales(self, count: int) -> None:
        """Adauga un numar de vanzari random

        Args:
            count (int): Numarul de vanzari random adaugate
        """
        titluri_genuri = [
            ("Robinson Crusoe", "Actiune"),
            ("O calatorie spre centrul pamantului", "Actiune"),
            ("In linie dreapta", "Actiune"),
            ("Jocul de domino", "Mister"),
            ("Cazemata", "Mister"),
            ("Bani de hartie", "Mister"),
            ("Agentul Cormac", "Fantezie"),
            ("Razboiul elitelor", "Fantezie"),
            ("Golul temporal", "Fantezie"),
            ("Soarele umbrit", "Groaza"),
            ("Focul alb", "Groaza"),
            ("Taietura finala", "Groaza"),
            ("Soapte de iubire", "Romantism"),
            ("Genul ala de fata", "Romantism"),
            ("Camasa lui", "Romantism"),
            ("Orion va rasari", "Science Fiction"),
            ("Marginea fundatiei", "Science Fiction"),
            ("Existenta", "Science Fiction"),
            ("Alice in tara oglinzilor", "Nuvela"),
            ("Colt alb", "Nuvela"),
            ("Proza", "Nuvela"),
            ("Zogru", "Thriller"),
            ("Iubirea croitoresei", "Thriller"),
            ("Ultima iluzie", "Thriller")
        ]

        iduri_folosite = [sale.id for sale in self.__sales]
        id_nou = 1
        new_random_sales = []

        for i in range(count):
            while id_nou in iduri_folosite:
                id_nou += 1

            titlu_nou, gen_nou = titluri_genuri[randrange(len(titluri_genuri) - 1)]
            pret_nou = float(randrange(10, 250))
            reducere_noua = choice(["none", "silver", "gold"])

            new_random_sales.append(Sale(id_nou, titlu_nou, gen_nou, pret_nou, reducere_noua))

            iduri_folosite.append(id_nou)    
            
        self.__sales.extend(new_random_sales)
        
        def remove_random_sales():
            self.__sales = list(set(self.__sales).difference(new_random_sales))
        
        self.__undo_operations.append([
            lambda: remove_random_sales(),
            lambda: self.__sales.extend(new_random_sales)
        ])
        
        self.__redo_operations.clear()