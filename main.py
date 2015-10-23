from objects.IntegerModP import IntegerModP as IntegerModP
from objects.PolynomialModP import PolynomialModP as PolynomialModP
from objects.FiniteField import FiniteField as FiniteField

# Aliases
IntModP = IntegerModP
PolyModP = PolynomialModP
FF = FiniteField

import code


def main():
    # Copies over all variables
    vars = globals().copy()
    vars.update(locals())
    # Creates an interactive console
    shell = code.InteractiveConsole(vars)
    shell.interact(banner="Interactive Python console for the purpose of testing the 2WF90 Assignment.\n"
                          "See documentation.pdf for instructions on use.")

if __name__ == '__main__':
    main()
