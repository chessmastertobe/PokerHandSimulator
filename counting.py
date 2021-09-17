# this program will generate combinations and permutations with and without repetition

#from Combinations import *

def generatePR():
    # pr comes from the combinations file (that we would have to create)
#    print(pr(5,3))
    n = 5
    count =  0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    print(count, i,j,k)
                    count += 1
def generateC():
    # c comes from the combinations file (that we would have to create)
#    print(c(5,3))
    n = 5
    count =  0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                print(count, i,j,k)
                count += 1

def generateCR():
    # cr comes from the combinations file (that we would have to create)
#    print(cr(5,3))
    n = 5
    count =  0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(count, i,j,k)
                count += 1


def main():
    generatePR()
    generateC()

main()
