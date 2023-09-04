#primtal = []

#while len(primtal) < 1001:
#    for tal in range(1,10000):
#        for i in range(3,tal-1):
#            if tal % i == 0:    
#                continue
#            else: 
#                   primtal.append(tal)

#print(primtal)

primtal = []

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = 2  # Start checking from 2, the first prime number

while len(primtal) < 1000:
    if is_prime(num):
        primtal.append(num)
    num += 1

print(primtal)