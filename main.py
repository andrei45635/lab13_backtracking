from backtracking_recursiv import BackRec
from backtracking_iterativ import back_iter

if __name__ == '__main__':
    lista = [0,1,-1,1,-1,0,0,1,-1,1,0,1]
    print('-----recursiv----\n')
    BackRec(lista, 0, [])
    print("-----iterativ-----\n")
    back_iter(lista, 3)