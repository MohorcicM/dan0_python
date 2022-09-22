#Naredi class student in fakulteta
"""
Student
-ocene (predmet, ocene)
-vpisna_st
-ime
-letnik

def:
    -vpis
    -izpis

Fakulteta
-spisek studentov

def:
    -oceni
    -napreduj
"""

class Student(object):
    ocene = {"IKT":-1, "OBS":-1, "ROS":-1}
    def __init__(self, vpisna_st, ime, letnik):
        self.vpisna_st = vpisna_st
        self.ime = ime
        self.letnik = letnik

    def oceni(predmet, ocena):
        pass

    def napreduj():
        pass

    def __del__(self):
        print("izbrisem studenta")

spisek_studentov = {}
class Fakulteta(object):
    
    def __init__(self):
        pass

    def vpis(ime, vpisna_st):
        spisek_studentov[ime] = vpisna_st
        

    def izpis():
        pass

fe_elektro = Fakulteta()
fe_elektro.vpis("Matej", 6846215)

print(spisek_studentov["Matej"])