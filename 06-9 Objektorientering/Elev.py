class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd

        if self.godkänd == True:
            self.glad = True
        else: 
            self.glad = False
    def presentera(self):
        print(f"Hej, Jag heter {self.namn}.")

elev1 = Elev("Alex", 18, True)

elev1.presentera()

if elev1.glad == True:
    print("Elev 1 är glad!")
else:
    print("Elev 1 är inte glad!")