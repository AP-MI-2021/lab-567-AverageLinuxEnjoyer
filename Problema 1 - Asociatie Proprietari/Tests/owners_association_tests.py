from Logic.owners_association import OwnersAssociation

def test_owners_association():
    association = OwnersAssociation()
    
    association.addExpense(1, 15, 200, "intretinere", "15.09.2021")
    
    expense = association.getExpense(1)
    
    assert expense.id == 1
    assert expense.apartment_number == 15
    assert expense.amount == 200
    assert expense.expense_type == "intretinere"
    assert expense.date == "15.09.2021"
    
    association.modifyExpense(1, 17, 300, "canal", "20.08.2021")
    
    assert expense.id == 1
    assert expense.apartment_number == 17
    assert expense.amount == 300
    assert expense.expense_type == "canal"
    assert expense.date == "20.08.2021"
    
    association.removeExpense(1)
    
    assert association.getExpense(1) == None