from Logic.sales_manager import SalesManager
from UserInterface.exceptionDecorator import valueErrorHandler

class CommandLine:
    accent_color = '\033[96m'
    normal_color = '\033[0m'
    
    def __init__(self, sales_manager: SalesManager):
        self.__sales_manager = sales_manager
        
    def help(self):
        a = CommandLine.accent_color
        n = CommandLine.normal_color
    
        print(f"""
    {a}help{n}                                                  - arata acest meniu
    
    {a}add{n}           ,<id>,<titlu>,<gen>,<pret>,<reducere>   - adauga o vanzare
    {a}remove{n}        ,<id>                                   - sterge o vanzare
    {a}edit{n}          ,<id>,<titlu>,<gen>,<pret>,<reducere>   - modifica o vanzare
    {a}discount{n}                                              - aplica discount-urile aferente
    {a}minprice{n}                                              - determina pretul minim pentru fiecare gen
    {a}order{n}                                                 - ordoneaza crescator vanzarile dupa pret
    {a}distinct titles{n}                                       - afiseaza numarul de titluri distincte pe gen
    
    {a}undo{n}
    {a}redo{n}
    
    {a}addrandom{n} ,<count>                                    - adauga un numar de vanzari random
    {a}showall{n}                                               - arata toate vanzarile
    {a}exit{n}                                                  - inchide programul
    """)       
    
    @valueErrorHandler
    def add(self, parameters: list):
        
        id = int(parameters[1])
        title = parameters[2]
        genre = parameters[3]
        price = int(parameters[4])
        discount_type = parameters[5]
        
        self.__sales_manager.addSale(id, title, genre, price, discount_type)
        
        print("Vanzare adaugata cu succes.")
        
    @valueErrorHandler
    def remove(self, parameters: list):
        
        id = int(parameters[1])
        
        self.__sales_manager.removeSale(id)
        print("Vanzare stearsa cu succes.")
        
    @valueErrorHandler
    def edit(self, parameters: list):
        
        id = int(parameters[1])
        title = parameters[2]
        genre = parameters[3]
        price = int(parameters[4])
        discount_type = parameters[5]
        
        self.__sales_manager.modifySale(id, title, genre, price, discount_type)
        print("Modificare efectuata cu succes.")
        
    def discount(self):
        self.__sales_manager.applyDiscounts()
        
    def minprice(self):
        c = CommandLine.accent_color
        n = CommandLine.normal_color
        
        dictionary = self.__sales_manager.getMinimumPricePerGenre()
        
        for genre, price in dictionary.items():
            print(f"{c + genre + ':' + n:<30} {price}")
        
    def distinctTitles(self):
        c = CommandLine.accent_color
        n = CommandLine.normal_color
        
        pairs_list = self.__sales_manager.getDistinctTitlesPerGenre()
        
        for genre, titles_num in pairs_list:
            print(f"{c + genre + ':' + n:<30} {titles_num}")
        
    @valueErrorHandler
    def addRandom(self, parameters: list):
        count = int(parameters[1])
        
        self.__sales_manager.addRandomSales(count)
        
        if count <= 0:
            print("Nu a fost adaugata nici o vanzare random.")
        elif count == 1:
            print("A fost adaugata o vanzare random.")
        elif count >= 2:
            print(f"Au fost adaugate {count} vanzari random.")
        
    def showAll(self):
        sales = self.__sales_manager.sales
        
        for sale in sales:
            print(sale)

        
    def run(self):
        shouldExit = False
        
        self.help()
        while not shouldExit:
            print("Introduceti comanda: (comenzile se separa prin ; iar parametrii unei comenzi prin ,)")
            
            raw_commands = input()
            
            commands = raw_commands.split(";")
            
            for command in commands:
                parameters = command.split(",")
                
                if parameters[0] == "help":
                    self.help()
                elif parameters[0] == "add":
                    self.add(parameters)
                elif parameters[0] == "remove":
                    self.remove(parameters)
                elif parameters[0] == "edit":
                    self.edit(parameters)
                elif parameters[0] == "discount":
                    self.discount()
                elif parameters[0] == "minprice":
                    self.minprice()
                elif parameters[0] == "order":
                    self.__sales_manager.orderSalesByPrice()
                    self.showAll()
                elif parameters[0] == "distinct titles":
                    self.distinctTitles()
                    
                elif parameters[0] == "undo":
                    self.__sales_manager.undo()
                elif parameters[0] == "redo":
                    self.__sales_manager.redo()
                    
                elif parameters[0] == "showall":
                    self.showAll()
                elif parameters[0] == "addrandom":
                    self.addRandom(parameters)
                elif parameters[0] == "exit":
                    shouldExit = True