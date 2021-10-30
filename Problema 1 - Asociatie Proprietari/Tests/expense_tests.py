from Domain.expense import Expense
from datetime import date

def test_expense():
    test = Expense(1, 33, 220, "intretinere", "10.09.2019")

    assert test.id == 1
    assert test.apartment_number == 33
    assert test.amount == 220
    assert test.expense_type == "intretinere"
    assert test.date == "10.09.2019"
