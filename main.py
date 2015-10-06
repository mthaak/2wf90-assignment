__author__ = 'Martin'
from objects.IntegerModP import IntegerModP


# TODO Put objects in subfolder
def main():
    i = IntegerModP(5, 5)
    j = IntegerModP(3, 5)
    print(i + j)
    pass
    # TODO Implement


if __name__ == '__main__':
    main()
