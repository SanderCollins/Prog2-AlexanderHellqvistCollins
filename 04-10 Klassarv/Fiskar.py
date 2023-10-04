class Djur:
    def __init__(self, namn):
        self.namn = namn
    
class Fagel(Djur):
    def __init__(self, namn, vinsgpann):
        super().__init__(namn)
        self.vinsgpann = vinsgpann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTänder):
        super().__init__(namn, maxdjup)
        self.antalTänder = antalTänder

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

torsk1 = Torsk("Felix", 100, 45)
torsk2 = Torsk("Hjalmar", 100, 25)
haj1 = Haj("Betty", 200, 250)

def fånga(haj: Haj, torsk: Torsk):
    return True if haj.maxdjup >= torsk.maxdjup and torsk.hastighet < 30 else False 

print(fånga(haj1, torsk2))
#print(f"R.I.P {torsk2.namn} will be missed.")