string = input("Skriv en mening som innehåller åtminstone en siffra.")
nummer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
siffror = 0


for karaktär in string:
    if karaktär in nummer:
        siffror += 1

print(f"Det fanns, {siffror} st siffror i meningen.")
