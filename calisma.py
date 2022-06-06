
class Human:
    def __init__(self, isim, yetenek):
        self.isim = isim
        self.yetenek = yetenek

class Polis(Human):
    def __init__(self, isim, yetenek, unvan):
        super().__init__(isim, yetenek)
        self.unvan = unvan

class Suclu(Human):
    def __init__(self, isim, yetenek, suc):
        super().__init__(isim, yetenek)
        self.suc = suc

class Halk(Human):
    def __init__(self, isim, yetenek, meslek):
        super().__init__(isim, yetenek)
        self.meslek = meslek

karakterler = []

while True:
    taraf = input("Karakterin taraf giriniz(Polis, Suclu, Halk)(cıkmak icin q): ")
    if taraf == "q":
        break
    if taraf == "Polis":
        isim = input("Karakterin ismini giriniz: ")
        yetenek = input("Karakterin yeteneğini giriniz: ")
        unvan = input("Karakterin unvanını giriniz: ")
        P1 = Polis(isim, yetenek, unvan)
        karakterler.append(P1)
    elif taraf == "Suclu":
        isim = input("Karakterin ismini giriniz: ")
        yetenek = input("Karakterin yeteneğini giriniz: ")
        suc = input("Karakterin sucunu giriniz: ")
        S1 = Suclu(isim, yetenek, suc)
        karakterler.append(S1)
    elif taraf == "Halk":
        isim = input("Karakterin ismini giriniz: ")
        yetenek = input("Karakterin yeteneğini giriniz: ")
        meslek = input("Karakterin meslegini giriniz: ")
        H1 = Halk(isim, yetenek, meslek)
        karakterler.append(H1)
    else:
        print("Lütfen 'Polis, Suclu, Halk' birini seciniz!")

for karakter in karakterler:
    print(karakter.isim)

