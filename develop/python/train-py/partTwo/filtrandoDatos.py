#!/usr/bin/python3
# ========================== Filtrando Datos ===========================
# by Cosmosacm... tomado de Platzi
#

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # list comprehensions
    allPythonDevs1 = [worker['name'] for worker in DATA if worker['language'] == 'python']
    # high order function
    allPythonDevs2 = list(filter(lambda worker: worker['language'] == 'python', DATA))
    allPythonDevs2 = list(map(lambda worker: worker['name'], allPythonDevs2)) 
    #
    # list comprehensions
    allPlatzyWorkers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    # high order function
    #allPlatzyWorkers2 = list(map())
    #
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    
    adults = list(map(lambda worker: worker['name'], DATA))
    
    oldPeople = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    #
    print('\nDesarrolladores de python solución 1: ')
    for worker in allPythonDevs1:
        print(worker)
    
    print('\nDesarrolladores de python solución 2: ')
    for worker in allPythonDevs2:
        print(worker)
    
    #
    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    
    print('Empleados de Platzi: ')
    for worker in allPlatzyWorkers:
        print(worker)
    #
    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    
    print('Mayores de 18 años: ')
    for worker in adults:
        print(worker)

    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    
    print('Mayores de 70 años: ')
    for worker in oldPeople:
        print(worker)


if __name__ == '__main__':
    run()