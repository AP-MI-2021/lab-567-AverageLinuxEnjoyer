from Tests.expense_tests import test_expense
from Tests.owners_association_tests import test_owners_association

def run_tests():
    test_expense()
    test_owners_association()

    print("Au fost trecute toate testele.")