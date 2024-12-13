DIM numbers[3]
FOR i = 0 TO 3
    numbers[i] = i * 2
    PRINT numbers[i]
NEXT 
REDIM numbers[5]
FOR i = 0 TO 5
    numbers[i] = i * 2
PRINT "Element 2"
PRINT numbers[1]