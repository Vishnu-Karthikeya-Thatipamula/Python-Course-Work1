'''
12 - factors
13 _ factors
14 - factors
'''
'''
N = int(input("Enter a num:"))
res = []
for i in range(1, N + 1):
    if N % i == 0:
        res.append(i)
print("The List of factors of",N,"are",res)
'''
