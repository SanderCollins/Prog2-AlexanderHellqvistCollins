# objektorientering
# ett objekt är en insants av en klass


class Bil:
    def __init__(self, färg, make):
        self.make = make
        self.färg = färg
    def omfärga(self):
        self.omfärga = self.färg

bilen = Bil("grön", "volvo")
         
print(bilen)