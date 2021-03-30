def generateMatrix(n):
    matrix=[]
    matrix=[ ['〇'] * n for _ in range(n)]
    return matrix

def displayMatrix(matrix,n):
    for x in range(0,n):    
        for y in range(0,n):
            print(matrix[x][y], end="")
        print("")

def detect(n,x,y):
    if((x-1<0 or (n==x+1)) or(y-1<0 or (n==y+1)) ):
        return False
    else:
        return True

def count(matrix,x,y,n):
    count=0
    if matrix[x-1][y-1]=="■":#1
        count=count+1
    if matrix[x][y-1]=="■":#2
        count=count+1
    if matrix[x+1][y-1]=="■":#3
        count=count+1
    if matrix[x-1][y]=="■":#4
        count=count+1
    if matrix[x+1][y]=="■":#6
        count=count+1
    if matrix[x-1][y+1]=="■":#7
        count=count+1
    if matrix[x][y+1]=="■":#8
        count=count+1
    if matrix[x+1][y+1]=="■":#9
        count=count+1
    return count

def count2(matrix,x,y,n):
    count=0
    if (x==0 and y==0):
        if matrix[x][y+1]=="■":
            count=count+1
        if matrix[x+1][y+1]=="■":
            count=count+1
        if matrix[x+1][y]=="■":
            count=count+1
    if (x==n-1 and y==0):
        if matrix[x-1][y]=="■":
            count=count+1
        if matrix[x-1][y+1]=="■":
            count=count+1
        if matrix[x][y+1]=="■":
            count=count+1
    if (x==0 and y==n-1):
        if matrix[x][y-1]=="■":
            count=count+1
        if matrix[x+1][y-1]=="■":
            count=count+1
        if matrix[x+1][y]=="■":
            count=count+1
    if (x==n-1 and y==n-1):
        if matrix[x][y-1]=="■":
            count=count+1
        if matrix[x-1][y]=="■":
            count=count+1
        if matrix[x-1][y-1]=="■":
            count=count+1
    if(y==0 and (x in range(1,n-1))):
        if matrix[x-1][y]=="■":#4
            count=count+1
        if matrix[x+1][y]=="■":#6
            count=count+1
        if matrix[x-1][y+1]=="■":#7
            count=count+1
        if matrix[x][y+1]=="■":#8
            count=count+1
        if matrix[x+1][y+1]=="■":#9
            count=count+1
    if(y==n-1 and (x in range(1,n-1))):
        if matrix[x-1][y-1]=="■":#1
            count=count+1
        if matrix[x][y-1]=="■":#2
            count=count+1
        if matrix[x+1][y-1]=="■":#3
            count=count+1
        if matrix[x-1][y]=="■":#4
            count=count+1
        if matrix[x+1][y]=="■":#6
            count=count+1
    if(x==0 and (y in range(1,n-1))):
        if matrix[x][y-1]=="■":#2
            count=count+1
        if matrix[x+1][y-1]=="■":#3
            count=count+1
        if matrix[x+1][y]=="■":#6
            count=count+1
        if matrix[x][y+1]=="■":#8
            count=count+1
        if matrix[x+1][y+1]=="■":#9
            count=count+1
    if(x==n-1 and (y in range(1,n-1))):
        if matrix[x-1][y-1]=="■":#1
            count=count+1
        if matrix[x][y-1]=="■":#2
            count=count+1
        if matrix[x-1][y]=="■":#4
            count=count+1
        if matrix[x-1][y+1]=="■":#7
            count=count+1
        if matrix[x][y+1]=="■":#8
            count=count+1
    return count

def numMatrix(n):
    matrix=[ [0] * n for _ in range(n)]
    return matrix

def add(matrix,num,n):
    c=0
    for x in range(0,n):
        for y in range(0,n):
            if(matrix[x][y]==0):
                    continue
            if  detect(n,x,y):
                c=count(matrix,x,y,n)
                num[x][y]=c
            else:
                c=count2(matrix,x,y,n)
                num[x][y]=c
            c=0
    #print(num)
    return num

def offSpring(numMatrix,n,matrix):
    for x in range(0,n):
        for y in range(0,n):
            original=matrix[x][y]
            if numMatrix[x][y]==3 :
                matrix[x][y]="■"
            elif numMatrix[x][y]==2 and original=="■":
                matrix[x][y]=original
            elif numMatrix[x][y]==2 and original=="〇":
                matrix[x][y]=original
            else:
                matrix[x][y]="〇"     
    return matrix

import copy

matrix=[]
n=int(input("n by n matrix"))
matrix=generateMatrix(n)

displayMatrix(matrix,n)

seed="■"
i=n
while (True):
    x=input("Input x: ")
    if(x=="e" ):
        break
    y=input("Input y: ")
    if(y=="e" ):
        break
    x=int(x)
    y=int(y)
    matrix[x][y]=seed

displayMatrix(matrix,n)

Flag=1
while(Flag==1):
    num=[]
    #Flag=1
    #num=numMatrix(n)
    num=[ [0] * n for _ in range(n)]#creat a matrix full of 0
    #Fine
    MatrixWithNum=[]
    MatrixWithNum=add(matrix,num,n)#count and then return a matrix with indexes

    displayMatrix(MatrixWithNum,n)#display the former number matrix

    print("--------------------------------------------------------------------------")
    matrixN=offSpring(MatrixWithNum,n,matrix)
    displayMatrix(matrixN,n)#The lives after evolution
    print("--------------------------------------------------------------------------")
    matrix=matrixN#update status
    #if(matrix !=matrixN):
    #    Flag=1
    #    matrix=matrixN#update status
    #else:
    #    Flag=0
