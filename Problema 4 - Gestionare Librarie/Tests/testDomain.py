from Domain.vanzare import creeazaVanzare, getId, getTitlu, getGen, getPret, getReducere

def testVanzare():
    vanzare = creeazaVanzare("2", "Fram, ursul polar", "Fictiune", 26.99, "silver")

    assert getId(vanzare) == "2"
    assert getTitlu(vanzare) == "Fram, ursul polar"
    assert getGen(vanzare) == "Fictiune"
    assert getPret(vanzare) == 26.99
    assert getReducere(vanzare) == "silver"