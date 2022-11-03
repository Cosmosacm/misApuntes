#!/usr/bin/python3
# ========================= Assert Statements ==========================
# by Cosmosacm... tomado de Platzi
# 

from numpy import number


def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print('\nD'numbers)


def write():
    names = ['Simón', 'Ramón', 'Peter', 'Juan', 'Lucas']
    with open('./files/nombres.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print('[!] Datos escritos correctamente...')

def run():
    read()
    write()


if __name__ == '__main__':
    run()