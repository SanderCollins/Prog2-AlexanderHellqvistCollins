
primtal = []
de_två = []

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

while len(de_två) < 1:
    if is_prime(num):
        produkt = 0
        if len(primtal) != 0:
            produkt = primtal[-1] * num
            
        primtal.append(num)
        if produkt >= 10000000000:
            de_två.append(primtal[-2])
            de_två.append(num)   
            break
    num += 1



print(de_två)