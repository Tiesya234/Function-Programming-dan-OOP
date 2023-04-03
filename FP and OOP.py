# Contoh program dalam paradigma FP
def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

def hitung_total(hitung, *args):
    total = args[0]
    for angka in args[1:]:
        total = hitung(total, angka)
    return total

# Contoh penggunaan fungsi hitung_total dengan fungsi perkalian dan pembagian
print(hitung_total(perkalian, 1, 2, 3, 4, 5))
print(hitung_total(pembagian, 10, 2, 5))


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
