primtal = []
primfaktorn = []

i = 0
nummer = 600851475143

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

num = 2

while i < nummer/100000:
    if is_prime == True:
        primtal.append(num)
        num += 1
        i += 1

print(primtal)

for tal in primtal:
    if nummer % tal == 0 and tal >= primfaktorn(0): 
        if len(primfaktorn) >= 1:
            primfaktorn.pop(0)
        else:
            primfaktorn.append(tal)
        

