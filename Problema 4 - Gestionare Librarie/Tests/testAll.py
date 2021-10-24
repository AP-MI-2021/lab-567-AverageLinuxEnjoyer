from Tests.testDomain import testVanzare
from Tests.testCRUD import testCRUD
from Tests.testDiscount import testAplicareDiscount
from Tests.testModificareGen import testModificareGen

def runTests():
    testVanzare()
    testCRUD()
    testAplicareDiscount()
    testModificareGen()