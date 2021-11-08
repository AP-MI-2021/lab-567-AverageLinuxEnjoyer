from Tests.all_tests import run_tests
from Logic.sales_manager import SalesManager
from UserInterface.menu import Menu
from UserInterface.command_line import CommandLine

def main():
    run_tests()
    
    a = '\033[96m'
    n = '\033[0m'
    
    interface_type = input(f"Ce fel de interfata vrei sa folosesti?\nCommand line {a}(c){n} sau Meniu {a}(m){n}?")
    
    sales_manager = SalesManager()
    
    if interface_type == "c":
        command_line = CommandLine(sales_manager)
        command_line.run()
    elif interface_type == "m":
        menu = Menu(sales_manager)
        menu.run()

if __name__ == "__main__":
    main()