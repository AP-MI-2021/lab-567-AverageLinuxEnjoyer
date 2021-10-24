from Tests.testDomain import testVanzare
from Tests.testCRUD import testCRUD
from Tests.testDiscount import testAplicareDiscount
from Tests.testModificareGen import testModificareGen
from Tests.testPretMinim import testPretMinimGen
from Tests.testOrdonareVanzari import testOrdonareVanzari
from Tests.testTitluriDistinctePerGen import testTitluriDistinctePerGen

def runTests():
    testVanzare()
    testCRUD()
    testAplicareDiscount()
    testModificareGen()
    testPretMinimGen()
    testOrdonareVanzari()
    testTitluriDistinctePerGen()