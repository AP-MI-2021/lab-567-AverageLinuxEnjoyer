from typing import Callable

def valueErrorHandler(function: Callable) -> Callable:
    """Decorator care encapsuleaza o intreaga functie intr-un try-except block.
    Destinata folosirii pe functii in care pot aparea ValueErrors

    Args:
        function (Callable): Functia care va fi encapsulata intr-un try-except block

    Returns:
        Callable: Functia care encapsuleaza functia data ca parametru
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError as ve:
            print("Error: ", ve)
    
    return wrapper
        
    