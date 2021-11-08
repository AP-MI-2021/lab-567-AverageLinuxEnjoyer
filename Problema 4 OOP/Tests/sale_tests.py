from Domain.sale import Sale

def test_sale():
    sale = Sale(2, "Harap Alb", "Fictiune", 24.99, "silver")
    
    assert sale.id              == 2
    assert sale.title           == "Harap Alb"
    assert sale.genre           == "Fictiune"
    assert sale.price           == 24.99
    assert sale.discount_type   == "silver"