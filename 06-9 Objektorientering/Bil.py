class bil:
    __maxhastighet = 0
    antalbilar = 0
    def __init__(self, __maxhastighet):
        self.__maxhastighet = __maxhastighet
        bil.antalbilar += 1
    @staticmethod
    def milestokm(miles):
        return 1.6093*miles
    def getmaxhastighet(self):
        return self.__maxhastighet
    def setmaxhastighet(self, __maxhastighet):
        self.__maxhastighet = __maxhastighet

print(bil.milestokm(20))

Volvo = bil(70)
Audi = bil(120)
bmw = bil(100)

print(bil.antalbilar)
print(Volvo.getmaxhastighet())

Volvo.setmaxhastighet(100) 
print(Volvo.getmaxhastighet())

#print(Volvo.maxhastighet)