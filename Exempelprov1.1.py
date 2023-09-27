rättnings_lista = []
input_sträng = input("skriv hur många kungar, damer, torn, löpare, hästar och bönder du har med ett mellanrum mellan varje")
try:
    schack_pjaser = input_sträng.split()
    for i in range(len(schack_pjaser)):
        schack_pjaser[i] = int(schack_pjaser[i])
        for i in range(6):
            if i == 0 or i == 1:
                if schack_pjaser[i] == 1:
                        rättnings_lista.append(0)
                else:
                        rättnings_lista.append(1-schack_pjaser[i]) 
            elif i == 2 or i == 3 or i == 4:
                if schack_pjaser[i] == 2:
                        rättnings_lista.append(0)
                else:
                        rättnings_lista.append(2-schack_pjaser[i]) 
            else:
                if schack_pjaser[i] == 8:
                        rättnings_lista.append(0)
                else:  
                        rättnings_lista.append(8-schack_pjaser[i]) 
    print(rättnings_lista)
except:
    print("fel input")