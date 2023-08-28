konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
ny_mening = ""

mening = input("skriv ett ord att översätta").lower()
for bokstav in mening:
    if bokstav in konsonanter:
        ny_mening += bokstav + "o" + bokstav
    else: 
        ny_mening += bokstav
print(ny_mening)

