DIM numbers[3]
DIM numbers2[4]
FOR i = 0 TO 2
    numbers[i] = i * 2
NEXT 
PRINT numbers[0]
PRINT numbers[1]
PRINT numbers[2]
numbers2[0] = 5
numbers[0]=numbers2[0]
PRINT numbers[0]