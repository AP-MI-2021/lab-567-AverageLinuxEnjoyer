from Logic.sales_manager import SalesManager

def test_crud():
    sales_manager = SalesManager()
    sales_manager.addSale(1, "Harap Alb", "Fictiune", 23.99, "silver")
    sales_manager.addSale(2, "Ion", "Realism", 50, "gold")
    
    assert sales_manager.sales[0].id            == 1
    assert sales_manager.sales[0].title         == "Harap Alb"
    assert sales_manager.sales[0].genre         == "Fictiune"
    assert sales_manager.sales[0].price         == 23.99
    assert sales_manager.sales[0].discount_type == "silver"
    
    assert sales_manager.sales[1].id            == 2
    assert sales_manager.sales[1].title         == "Ion"
    assert sales_manager.sales[1].genre         == "Realism"
    assert sales_manager.sales[1].price         == 50
    assert sales_manager.sales[1].discount_type == "gold"
    
    assert len(sales_manager.sales) == 2
    
    sales_manager.removeSale(1)
    
    assert len(sales_manager.sales) == 1
    
    sales_manager.modifySale(2, "Moara cu noroc", "Realism", 43, "none")
    
    assert sales_manager.sales[0].id            == 2
    assert sales_manager.sales[0].title         == "Moara cu noroc"
    assert sales_manager.sales[0].genre         == "Realism"
    assert sales_manager.sales[0].price         == 43
    assert sales_manager.sales[0].discount_type == "none"

def test_discount():
    sales_manager = SalesManager()
    
    sales_manager.addSale(1, "Fram, ursul polar",   "Fictiune", 30.0,   "silver")
    sales_manager.addSale(2, "Harry Potter",        "Fictiune", 35.0,   "gold")
    sales_manager.addSale(3, "Moara cu noroc",      "Actiune",  13.99,  "none")

    sales_manager.applyDiscounts()
    
    assert sales_manager.getByID(1).price == 28.5
    assert sales_manager.getByID(2).price == 31.5
    assert sales_manager.getByID(3).price == 13.99

def test_minimum_price():
    sales_manager = SalesManager()

    sales_manager.addSale(1, "Ion",                     "Realist",      20.0,   "none")
    sales_manager.addSale(2, "Moara cu noroc",          "Realist",      70.0,   "none")
    sales_manager.addSale(3, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    sales_manager.addSale(4, "Alexandru Lapusneanu",    "Realist",      25.99,  "none")
    sales_manager.addSale(5, "Ultima noapte",           "Psihologie",   64.0,   "none")
    sales_manager.addSale(6, "Harap Alb",               "Fantastic",    120.0,  "none")

    assert sales_manager.getMinimumPricePerGenre() == {"Realist":20.0, "Psihologie":15.0, "Fantastic": 120}

def test_order_sales():
    sales_manager = SalesManager()

    sales_manager.addSale(1, "Ion",                     "Realist",      20.0,   "none")
    sales_manager.addSale(2, "Moara cu noroc",          "Realist",      70.0,   "none")
    sales_manager.addSale(3, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    sales_manager.addSale(4, "Alexandru Lapusneanu",    "Realist",      25.99,  "none")
    sales_manager.addSale(5, "Ultima noapte",           "Psihologie",   64.0,   "none")
    sales_manager.addSale(6, "Harap Alb",               "Fantastic",    120.0,  "none")

    sales_manager.orderSalesByPrice()

    assert [sale.price for sale in sales_manager.sales] == [15.0, 20.0, 25.99, 64.0, 70.0, 120.0]

def test_distinct_titles():
    sales_manager = SalesManager()

    sales_manager.addSale(1, "Ion",                     "Realist",      20.0,   "none")
    sales_manager.addSale(7, "Ion",                     "Realist",      20.0,   "none")
    sales_manager.addSale(2, "Moara cu noroc",          "Realist",      70.0,   "none")
    sales_manager.addSale(3, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    sales_manager.addSale(8, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    sales_manager.addSale(9, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    sales_manager.addSale(4, "Alexandru Lapusneanu",    "Realist",      25.99,  "none")
    sales_manager.addSale(5, "Ultima noapte",           "Psihologie",   64.0,   "none")
    sales_manager.addSale(10,"Ultima noapte",           "Psihologie",   64.0,   "none")
    sales_manager.addSale(6, "Harap Alb",               "Fantastic",    120.0,  "none")
    sales_manager.addSale(11,"Harap Alb",               "Fantastic",    120.0,  "none")

    assert sales_manager.getDistinctTitlesPerGenre() == [('Realist', 3), ('Psihologie', 2), ('Fantastic', 1)]

def test_undo_redo():
    # 1 start program
    sales_manager = SalesManager()
    
    # 2 add o1
    sales_manager.addSale(1, "Ion",                     "Realist",      20.0,   "none")
    assert len(sales_manager.sales) == 1
    
    # 3 add o2
    sales_manager.addSale(2, "Moara cu noroc",          "Realist",      70.0,   "none")
    assert len(sales_manager.sales) == 2
    
    # 4 add o3
    sales_manager.addSale(3, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    assert len(sales_manager.sales) == 3
    
    # 5 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 2
    
    # 6 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 1
    
    # 7 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 0
    
    # 8 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 0
    
    # 9 add o1,o2,o3
    sales_manager.addSale(1, "Ion",                     "Realist",      20.0,   "none")
    sales_manager.addSale(2, "Moara cu noroc",          "Realist",      70.0,   "none")
    sales_manager.addSale(3, "Enigma Otiliei",          "Psihologie",   15.0,   "none")
    assert len(sales_manager.sales) == 3
    
    # 10 redo
    sales_manager.redo()
    assert len(sales_manager.sales) == 3
    
    # 11 undo, undo
    sales_manager.undo()
    sales_manager.undo()
    assert len(sales_manager.sales) == 1
    
    # 12 redo
    sales_manager.redo()
    assert len(sales_manager.sales) == 2
    
    # 13 redo
    sales_manager.redo()
    assert len(sales_manager.sales) == 3
    
    # 14 undo, undo
    sales_manager.undo()
    sales_manager.undo()
    assert len(sales_manager.sales) == 1
    
    # 15 add o4
    sales_manager.addSale(4, "Alexandru Lapusneanu",    "Realist",      25.99,  "none")
    assert len(sales_manager.sales) == 2
    
    # 16 redo
    sales_manager.redo()
    assert len(sales_manager.sales) == 2
    
    # 17 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 1
    
    # 18 undo
    sales_manager.undo()
    assert len(sales_manager.sales) == 0

    # 19 redo, redo
    sales_manager.redo()
    sales_manager.redo()
    assert len(sales_manager.sales) == 2
    
    # 20 redo
    sales_manager.redo()
    assert len(sales_manager.sales) == 2


def test_sales_manager():
    test_crud()
    test_discount()
    test_minimum_price()
    test_order_sales()
    test_distinct_titles()
    test_undo_redo()