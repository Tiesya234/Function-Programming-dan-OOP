# Contoh kode program dalam paradigma FP
def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

# Contoh penggunaan fungsi perkalian dan pembagian
print(perkalian(4, 5))
print(pembagian(10,5))


# Contoh program dalam paradigma OOP
class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return (self.panjang * self.lebar * self.tinggi)

# Contoh penggunaan class Balok
balok1 = Balok(4, 5, 6)
print(balok1.luas())
