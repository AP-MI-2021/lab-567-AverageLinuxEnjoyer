from Tests.testAll import runTests
from UserInterface.meniu import runMenu
from UserInterface.command_line_console import run_command_line

def main():
    runTests()

    vanzari = []
    run_command_line(vanzari)
    
if __name__ == "__main__":
    main()