def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    c=[]
    if len(a[0]) != len(b):
        return -1 
    for i in range(len(a)):
        temp =[]
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k]*b[k][j]
            temp.append(total)
        c.append(temp)
    return c