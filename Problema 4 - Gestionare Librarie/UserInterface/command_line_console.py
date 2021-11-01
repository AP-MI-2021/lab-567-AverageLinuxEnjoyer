from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare
from Domain.vanzare import toString
from UserInterface.exceptionDecorator import valueErrorHandler

def help():
    print("""
    help                                        - arata acest meniu
    add,<id>,<titlu>,<gen>,<pret>,<reducere>    - adauga o vanzare
    remove,<id>                                 - sterge o vanzare
    edit,<id>,<titlu>,<gen>,<pret>,<reducere>   - modifica o vanzare
    showall                                     - arata toate vanzarile
    exit                                        - inchide programul
    """)

@valueErrorHandler
def add(vanzari: list, parameters: list) -> list:
    
    id = parameters[1]
    titlu = parameters[2]
    gen = parameters[3]
    pret = int(parameters[4])
    reducere = parameters[5]
    
    print("Vanzare adaugata.")
    return adaugareVanzare(id, titlu, gen, int(pret), reducere, vanzari)

@valueErrorHandler
def remove(vanzari: list, parameters: list) -> list:
    
    id = parameters[1]
    
    print("Stergere efectuata.")
    return stergereVanzare(id, vanzari)

@valueErrorHandler
def edit(vanzari: list, parameters: list) -> list:
    
    id = parameters[1]
    titlu = parameters[2]
    gen = parameters[3]
    pret = int(parameters[4])
    reducere = parameters[5]
    
    print("Modificare efectuata.")
    
    return modificareVanzare(id, titlu, gen, pret, reducere, vanzari)

def showAll(vanzari: list):
    for vanzare in vanzari:
        print(toString(vanzare))

def run_command_line(vanzari: list):
    
    shouldExit = False
    while not shouldExit:
        print("Introduceti comanda: (comenzile se separa prin ; iar parametrii unei comenzi prin ,)")
        raw_commands = input()
        
        commands = raw_commands.split(";")
        for command in commands:
            parameters = command.split(",")
            
            if parameters[0] == "help":
                help()
            elif parameters[0] == "add":
                vanzari = add(vanzari, parameters)
            elif parameters[0] == "remove":
                vanzari = remove(vanzari, parameters)
            elif parameters[0] == "edit":
                vanzari = edit(vanzari, parameters)
            elif parameters[0] == "showall":
                showAll(vanzari)
            elif parameters[0] == "exit":
                shouldExit = True
        
            
        
        
        