


class Pravokotnik(object):
    barva = "rdeca"
    def __init__(self, a , b): #__init__ je konstruktor(obstaja tudi destruktor), to dodamo vedno
        print("sem nov pravokotnik")
        #self #tocno ta pravokotnik v katerem smo sedaj
        self.a = a
        self.b = b
    
    def ploscina(self):
        return self.a * self.b

    def obseg(self):
        return 2*self.a + 2*self.b

    def __del__(self): #__del__ destruktor ta izbrise pravokotnik iz spomina
        print("Izbrisem pravokotnik")

class Kvadrat(Pravokotnik): #sedaj imama kvadrat enake atribute kot pravokotnik
    def __init__(self, a):
        super(Kvadrat, self).__init__(a, a)


if __name__ == "__main__": # to nam sedaj varuje, da ko example.py importamo v drug file se spodnji del kode ne izvede
    prav = Pravokotnik(5.0, 4.0)
    prav1 = Pravokotnik(5.3, 4.0)
    print(prav.a)
    print(prav1.a)
    print(prav.barva)
    print(prav1.barva)

    kv1 = Kvadrat(4.0)
    print(kv1.ploscina())

    del prav #tu klicemo destruktor 