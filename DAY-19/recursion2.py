# print 10...1
'''
def display(n):
    if n == 11:
        return
    print(n)
    display(n + 1)

display(1)
def display1(n):
    if n == 11:
        return 
    display(n + 1)
    print(n)
display1(1)


def display3(s,n):
    if n== len(s):
        return
    display3(s,n+1)
    print(s[n], end =' ')

display3("Codegnan",0)



def display(S, n, i):
    if n == int((len(S) - 1)/i):
        return
    print(S[n:n+i], end =' ')
    n = n + i
    display(S, n, i)
S = 'Python Programming'
i = (input())
display(S, 0, i)



def display(L, n):
    if n == len(L):
        return
    s = 0
    return L[n] + display(L,n + 1)

L = [11,12,13,45,16,78,89]
print(display(L, 0))



def display(L):
    if L == 0:
        return 0 
    return L % 10 + display(L//10)
L = 43567
print(display(L))

def display(N):
    if N == 1:
        return 1
    return N * display(N - 1)
N = int(input())
print(display(N))
'''

def display_recursive(N, P, L):
    if L == 0:
        return
    display_recursive(P, N + P, L - 1)
    print(N, end=" ")

if __name__ == '__main__':
    N = int(input())
    P = int(input())
    L = int(input())
    display_recursive(N, P, L)


