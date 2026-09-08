#'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
'''
  0 1 2 3 4 5
0 * * * * * * 
1 *         *
2 *         *
3 *         * 
4 *         * 
5 * * * * * *

n = int(input("Enter the range:"))
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == n-1 or j == n - 1:
            print("*",end =" ")
        else:
            print(" ", end=" ") 
    print()

  0 1 2 3 4 5
0 * * * * * * 
1 *         *
2 * * * * * *
3 *         * 
4 *         * 
5 * * * * * *

n = int(input("Enter the size:"))
m = n //2
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == m or j == n - 1:
            print("*",end =" ")
        else:
            print(" ", end=" ")
    print()

  0 1 2 3 4 5
0 * * * * * * 
1 *         
2 * * * * * *
3 *         
4 *         
5 * * * * * *

n = int(input("Enter the size:"))
m = n //2
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == m or i == n - 1:
            print("*",end =" ")
        else:
            print(" ", end=" ")
    print()

    
  0 1 2 3
0 * * * *
1     *
2   *
3 * * * * 


n = int(input("Enter the range:"))
for i in range(n):
    for j in range(n):
        if i == 0  or i + j == n- 1 or i == n-1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

    
  0 1 2 3 4 5
0 * * * * * * 
1 *         
2 * 
3 *         
4 *         
5 * * * * * *


n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == n - 1:
            print("*",end =" ")
        else:
            print(" ", end=" ")
    print()

  0 1 2 3 4 5
0 * * * * * * 
1 *         
2 * 
3 *     * * *
4 *         *
5 * * * * * *



n = int(input("Enter the size:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or  j == 0 or i == n - 1 or (j== n - 1 and i >= m) or (i == m and j >= m):
            print("*",end =" ")
        else:
            print(" ", end=" ")
    print()

  0 1 2 3 4 5
0 *         * 
1 *         *
2 *         *   
3 * * * * * *
4 *         *
5 *         *

n = int(input("Enter the size:"))
m = n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == m:
            print("*", end= " ")
        else:
            print(" ", end = " ")
    print()

  0 1 2 3 4 5
0 * * * * * * 
1       *
2       *
3       *
4       *
5 * * * * * *


n = int(input("Enter the size:"))
m = n // 2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == m:
            print("*", end= " ")
        else:
            print(" ", end = " ")
    print()

  0 1 2 3 4 5
0 *
1   *       * 
2     *   *
3       *     
4     *   *
5   *       *

n = int(input("Enter the size:"))
m = n // 2
for i in range(n):
    for j in range(n):
        if i == j or i+j == n - 1:
            print("*", end= " ")
        else:
            print(" ", end = " ")
    print()

  0 1 2 3 4 5
0 * * * * * * 
1       *
2       *
3       *
4       *
5 * * * * 
n = int(input("Enter the size:"))
m = n // 2
for i in range(n):
    for j in range(n):
        if i == 0 or j == n //2 or (i == n - 1 and j <= n //2):
            print("*", end= " ")
        else:
            print(" ", end = " ")
    print()


  0 1 2 3 4 
0 *       *
1 *   *
2 * *
3 *   *                             
4 *       *  
'''

n = int(input("Enter the size: "))
m = n // 2
for i in range(n):
    for j in range(n):
        # j == 0 prints the left vertical line
        # j == max(1, abs(i - m) * 2) calculates the exact diagonal 'V' shape
        if j == 0 or j == max(1, abs(i - m) * 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
