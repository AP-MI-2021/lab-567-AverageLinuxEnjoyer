

class Sale:
    def __init__(self, id: int, title: str, genre: str, price: float, discount_type: str):
        """Constructorul unui obiect de tip Sale

        Args:
            id (int): ID-ul vanzarii
            title (str): Titlul cartii vandute
            genre (str): Genul cartii vandute
            price (float): Pretul cartii
            discount_type (str): Tipul de discount (none/silver/gold)
        """
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__price = price
        
        if discount_type not in ("none", "silver", "gold"):
            raise ValueError('Acest tip de discount nu exista. Reincercati cu "none", "silver" sau "gold".')
        else:
            self.__discount_type = discount_type
    
    @property
    def id(self) -> int:
        """Getter ID"""
        return self.__id
    
    @property 
    def title(self) -> str:
        """Getter titlu"""
        return self.__title
    
    @property
    def genre(self) -> str:
        """Getter gen"""
        return self.__genre
    
    @genre.setter
    def genre(self, new_genre: str) -> None:
        """Setter gen"""
        self.__genre = new_genre
    
    @property
    def price(self) -> float:
        """Getter pret"""
        return self.__price
    
    @price.setter
    def price(self, new_price: float) -> None:
        """Setter amount"""
        self.__price = new_price
    
    @property 
    def discount_type(self) -> bool:
        """Getter tip de reducere"""
        return self.__discount_type
    
    def __str__(self) -> str:
        """Overload la functia de conversie in string

        Returns:
            str: Elementele vanzarii formatate intr-un string
        """
        return f"{'Id: ' + str(self.id):<10} {'Titlu: ' + self.title:<45}"\
               f"{'Gen: ' + self.genre:<25} {'Pret: ' + str(round(self.price, 2)):<13}"\
               f"Tip reducere: {self.discount_type}"