# Author: Uckan
# -*- coding: utf-8 -*-

# This code is implementation of a desing pattern called Chain of Responsibilty useful for large if/else cases for the book location visiual

class Handler:
    def __init__(self):
        self._next_handler = None


    # Set up the next handler   
    def set_next(self, handler):

        self._next_handler = handler
       
        return handler   # Return the handler for method chaining

    # Method to pass on the next handler if not the case. Using polymorphism for every handler 
    def handle(self, letter, number):
        if self._next_handler:
            return self._next_handler.handle(letter, number)
        else:
            print(letter ,number , "cant return")         
            return None


# Handlers for A group

class A1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'A' and number == 1:
            return (900, 300)
        else:
            return super().handle(letter, number)

class A2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'A' and number == 2:
            return (900, 300 + 550)
        else:
            return super().handle(letter, number)

class A3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'A' and number == 3:
            return (900, 300 + 2 * 550)
        else:
            return super().handle(letter, number)

class A4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'A' and number == 4:
            return (900, 300 + 3 * 550)
        else:
            return super().handle(letter, number)

class A5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'A' and number == 5:
            return (900, 300 + 4 * 550)
        else:
            return super().handle(letter, number)

# Handlers for B group

class B1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'B' and number == 1:
            return (2000, 300)
        else:
            return super().handle(letter, number)

class B2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'B' and number == 2:
            return (2000, 300 + 550)
        else:
            return super().handle(letter, number)

class B3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'B' and number == 3:
            return (2000, 300 + 2 * 550)
        else:
            return super().handle(letter, number)

class B4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'B' and number == 4:
            return (2000, 300 + 3 * 550)
        else:
            return super().handle(letter, number)

class B5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'B' and number == 5:
            return (2000, 300 + 4 * 550)
        else:
            return super().handle(letter, number)


# Handlers for C group

class C1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'C' and number == 1:
            return (3100, 300)
        else:
            return super().handle(letter, number)

class C2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'C' and number == 2:
            return (3100, 300 + 550)
        else:
            return super().handle(letter, number)

class C3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'C' and number == 3:
            return (3100, 300 + 2 * 550)
        else:
            return super().handle(letter, number)

class C4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'C' and number == 4:
            return (3100, 300 + 3 * 550)
        else:
            return super().handle(letter, number)

class C5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'C' and number == 5:
            return (3100, 300 + 4 * 550)
        else:
            return super().handle(letter, number)


# Handlers for D group

class D1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'D' and number == 1:
            return (1100, 400)
        else:
            return super().handle(letter, number)

class D2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'D' and number == 2:
            return (1100, 400 + 500)
        else:
            return super().handle(letter, number)

class D3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'D' and number == 3:
            return (1100, 400 + 2 * 500)
        else:
            return super().handle(letter, number)

class D4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'D' and number == 4:
            return (1100, 400 + 3 * 500)
        else:
            return super().handle(letter, number)

class D5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'D' and number == 5:
            return (1100, 400 + 4 * 500)
        else:
            return super().handle(letter, number)


# Handlers for E group

class E1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'E' and number == 1:
            return (2150, 400)
        else:
            return super().handle(letter, number)

class E2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'E' and number == 2:
            return (2150, 400 + 500)
        else:
            return super().handle(letter, number)

class E3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'E' and number == 3:
            return (2150, 400 + 2 * 500)
        else:
            return super().handle(letter, number)

class E4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'E' and number == 4:
            return (2150, 400 + 3 * 500)
        else:
            return super().handle(letter, number)

class E5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'E' and number == 5:
            return (2150, 400 + 4 * 500)
        else:
            return super().handle(letter, number)


# Handlers for F group

class F1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'F' and number == 1:
            return (3200, 400)
        else:
            return super().handle(letter, number)

class F2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'F' and number == 2:
            return (3200, 400 + 500)
        else:
            return super().handle(letter, number)

class F3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'F' and number == 3:
            return (3200, 400 + 2 * 500)
        else:
            return super().handle(letter, number)

class F4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'F' and number == 4:
            return (3200, 400 + 3 * 500)
        else:
            return super().handle(letter, number)

class F5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'F' and number == 5:
            return (3200, 400 + 4 * 500)
        else:
            return super().handle(letter, number)


# Handlers for G group since G is a different image its x and y coordinates are handled differnet then others

class G1Handler(Handler):
    def handle(self, letter, number):
        if letter == 'G' and number == 1:
            return (1200, 600)
        else:
            return super().handle(letter, number)

class G2Handler(Handler):
    def handle(self, letter, number):
        if letter == 'G' and number == 2:
            return (1200, 600 + 700)
        else:
            return super().handle(letter, number)

class G3Handler(Handler):
    def handle(self, letter, number):
        if letter == 'G' and number == 3:
            return (1200, 600 + 2 * 700)
        else:
            return super().handle(letter, number)

class G4Handler(Handler):
    def handle(self, letter, number):
        if letter == 'G' and number == 4:
            return (1200, 600 + 3 * 700)
        else:
            return super().handle(letter, number)

class G5Handler(Handler):
    def handle(self, letter, number):
        if letter == 'G' and number == 5:
            return (1200, 600 + 4 * 700)
        else:
            return super().handle(letter, number)


def setup_chain():
    # Start with the first handler for 'A1'
    handler_chain = A1Handler()
    last_handler = handler_chain  # Keep track of the last handler added
    
    # Chain handlers for 'A' group
    last_handler = last_handler.set_next(A2Handler()).set_next(A3Handler()).set_next(A4Handler()).set_next(A5Handler())
    
    # Chain handlers for 'B' group
    last_handler = last_handler.set_next(B1Handler()).set_next(B2Handler()).set_next(B3Handler()).set_next(B4Handler()).set_next(B5Handler())
    
    # Chain handlers for 'C' group
    last_handler = last_handler.set_next(C1Handler()).set_next(C2Handler()).set_next(C3Handler()).set_next(C4Handler()).set_next(C5Handler())
    
    # Chain handlers for 'D' group
    last_handler = last_handler.set_next(D1Handler()).set_next(D2Handler()).set_next(D3Handler()).set_next(D4Handler()).set_next(D5Handler())
    
    # Chain handlers for 'E' group
    last_handler = last_handler.set_next(E1Handler()).set_next(E2Handler()).set_next(E3Handler()).set_next(E4Handler()).set_next(E5Handler())
    
    # Chain handlers for 'F' group
    last_handler = last_handler.set_next(F1Handler()).set_next(F2Handler()).set_next(F3Handler()).set_next(F4Handler()).set_next(F5Handler())
    
    # Chain handlers for 'G' group
    last_handler = last_handler.set_next(G1Handler()).set_next(G2Handler()).set_next(G3Handler()).set_next(G4Handler()).set_next(G5Handler())

    return handler_chain


def get_coordinates(letter , number):
    handler_chain = setup_chain()
    coordinates = handler_chain.handle(letter , number)
    if coordinates:
        return coordinates
    else:
        print("The shelf group and number doesnt exist")
