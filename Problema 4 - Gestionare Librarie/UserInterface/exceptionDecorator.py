from typing import Callable

def valueErrorHandler(function: Callable) -> Callable:
    """Decorator care encapsuleaza o intreaga functie intr-un try-except block.
    Destinata folosirii pe functii din UserInterface care au ca parametru si returneaza o lista.

    Args:
        function (Callable): Functia care va fi encapsulata intr-un try-except block

    Returns:
        Callable: Functia care encapsuleaza functia data ca parametru
    """
    def wrapper(vanzari: list):
        try:
            return function(vanzari)
        except ValueError as ve:
            print("Error: ", ve)
            
        return vanzariz
    
    return wrapper
        
    