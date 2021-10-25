from Tests.testAll import runTests
from UserInterface.meniu import runMenu

def main():
    runTests()

    vanzari = []
    runMenu(vanzari)
    
if __name__ == "__main__":
    main()

    