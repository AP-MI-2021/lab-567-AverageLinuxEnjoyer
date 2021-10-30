from Tests.all_tests import run_tests
from Logic.owners_association import OwnersAssociation
from UserInterface.menu import Menu

def main():
    run_tests()
    
    owners_association = OwnersAssociation()
    menu = Menu(owners_association)
    
    menu.run_menu()
    

if __name__ == "__main__":
    main()