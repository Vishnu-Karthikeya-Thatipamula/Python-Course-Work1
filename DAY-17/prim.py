'''
def is_prime(n):
    prime = False
    count = 0
    for i in range(2,n+1):
        if n % i == 0:
            count += 1
            
    if count > 1:
        prime = False
    else:
        prime = True

    return prime

n = int(input("Enter the number:"))
print(is_prime(n))
'''
if __name__ == '__main__':
    
    studentsrecord = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        element = [name, score]
        print(studentsrecord.append)