#!/usr/bin/python3
# ======================= Lists and Dictionaries =======================
# by Cosmosacm...
# 

def run():
    myList = [1, 'Hello', True, 4.2]
    myDict = {'firstname': 'Neron', 'lastname': 'Navarrete'}
    superList =[
        {'firstname': 'Miguel', 'lastname': 'Servantes'},
        {'firstname': 'Leonardo', 'lastname': 'Da Vinci'},
        {'firstname': 'Rafael', 'lastname': 'Sanzio'},
        {'firstname': 'Donatello', 'lastname': 'Di Niccolo'},
        {'firstname': 'Carlos', 'lastname': 'Chaplin'}
    ]
    superDict = {
        'natural_nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'integer_nums': [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'float_nums': [-4.6, -3.3, -2.7, -1.2, 0.9, 1.3, 2.5, 3.8, 4.1, 5.4]
    }
    #
    for i, j in superDict.items():
        print(i, '-', j)

if __name__ == '__main__':
    run()