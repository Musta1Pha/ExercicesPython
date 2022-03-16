"""EXERCICE 01"""

'''def Function():
    x = float(input("Entrer la longueur du premier cote "))
    y = float(input("Entrer la longueur du Deuxieme cote "))
    z = float(input("Entrer la longueur du Troisieme cote "))
    if x==y and x==z and y==z:
        print('Triangle equilateral')
    elif x!=y and x!=z and y!=z:
        print('Triangle scalene')
    else:
        print('Triangle isocele')

"""EXERCICE 02"""

Function() '''
'''def Function2():
    s = 0
    i = 0
    x = int(input())
    while x!=0:    
        s += x
        i += 1
        x = int(input())
    if i == 0:
        print('Error')    
    else: return s/i

n = Function2()
print('la moyenne est ',n)'''

"""EXERCICE 03"""

"""def FunctionInt():
    List = []
    while True:
        x = int(input())
        if not x:
            List2 = []
            for i in range(len(List)): 
                List2.append(min(List))
                List.remove(min(List))
            return List2    
        else:
            List.append(x)


NvList = FunctionInt()
print(NvList) """

"""EXERCICE 04"""

'''def DecToBin(N):
    List = []
    while N!=0:
        List.insert(0,N%2)
        N = N//2
    List.insert(0,0)    
    return List

List = DecToBin(30)
print(List)'''

"""EXERCICE 05"""

'''def BinToDec(List):
    n = len(List)
    S = 0
    for i in List:
        S += (i * (2** (n-1)))
        n -= 1
    print(S)    

List = [0,1,1,1,1,0]
BinToDec(List)'''
