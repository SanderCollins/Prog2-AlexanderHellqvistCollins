from datetime import date
class Student:
    skola = ""
    def __init__(self, namn, personnr):
        self.__namn = namn
        self.__personnr = personnr
    def get_namn(self):
        return self.__namn
    def get_alder(self):
        year = int(self.__personnr[:2])
        month = int(self.__personnr[2:4])
        day = int(self.__personnr[4:6])
        today = date.today()
        idag = today.strftime("%y%m%d")
        studentAlder = int(idag[:2])-year
        print(day)
        print(idag[4:6])
        if int(idag[2:4]) < month:
            studentAlder -= 1
        elif int(idag[2:4]) == month and int(idag[4:6]) > day:
            studentAlder -= 1
        print(f"You are {studentAlder} years old")
    def Student(self, namn):
        namn = Student(namn)

Alex = Student("Alex", "050926")
print(Alex.get_namn())
print(Alex.get_alder())