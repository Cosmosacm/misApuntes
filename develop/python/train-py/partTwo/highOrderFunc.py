#!/usr/bin/python3
# ======================== High Order Functions ========================
# by Cosmosacm... tomado de Platzi
#

def saludo(func):
    func()


def hola():
    print('Hola buen día!!!')


def adios():
    print('Adios!!!')


def run():
    saludo(hola)
    saludo(adios)


if __name__ == '__main__':
    run()