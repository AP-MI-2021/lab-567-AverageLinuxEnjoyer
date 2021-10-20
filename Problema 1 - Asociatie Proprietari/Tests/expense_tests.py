from Domain.expense import Expense, ExpenseType
from datetime import date

def test_expense():
    test = Expense(1, 220, ExpenseType.MAINTAINANCE, "10.09.2019")

    assert test.apartment_number == 1
    assert test.amount == 220
    assert test.expense_type == ExpenseType.MAINTAINANCE
    assert test.date == date(2019,9,10)
