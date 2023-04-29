class Araba:
    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.hiz = 0

    def __str__(self):
        return f"{self.renk} {self.marka} {self.model}"

    def __repr__(self):
        return f"Araba(marka='{self.marka}', model='{self.model}', renk='{self.renk}')"

    def __eq__(self, other):
        return self.marka == other.marka and self.model == other.model and self.renk == other.renk

    def __lt__(self, other):
        return self.hiz < other.hiz

    def hizlan(self, hiz_degisim):
        self.hiz += hiz_degisim

    def fren_yap(self, hiz_degisim):
        self.hiz -= hiz_degisim



araba1 = Araba("BMW", "M3", "Siyah")
araba2 = Araba("Mercedes", "C200", "Gri")
araba3 = Araba("BMW", "M3", "Siyah")

print(araba1) # Siyah BMW M3
print(repr(araba1)) # Araba(marka='BMW', model='M3', renk='Siyah')

if araba1 == araba2:
    print("araba1 ve araba2 eşit")
else:
    print("araba1 ve araba2 eşit değil")

if araba1 == araba3:
    print("araba1 ve araba3 eşit")
else:
    print("araba1 ve araba3 eşit değil")

araba1.hizlan(50)
araba2.hizlan(70)

if araba1 < araba2:
    print(f"{araba1} daha yavaş")
else:
    print(f"{araba2} daha yavaş")


class toplama:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def __add__(self, other):
        return self.sayi1 + other.sayi1 , self.sayi2 + other.sayi2
    def __gt__(self, other):
        return self.sayi1 > other.sayi1
    def __eq__(self, other):
        return self.sayi1 == other.sayi1 and self.sayi2 == other.sayi2
    def __len__(self):
        if self.sayi1 > 20:
            print("Sayı 20den bölönebilir")
        else:
            print("Sayı 20den bölönemez")
ilksayi = toplama(30,40)
ikincisayi = toplama(50,20)
print(ilksayi > ikincisayi)
print(ilksayi + ikincisayi)
print(ilksayi == ikincisayi)
print(len(ilksayi))
print(len(ikincisayi))

"""
Tabii ki! İşte bazı yaygın olarak kullanılan özel metodlar:

- `__init__(self, ...)` : Bir sınıfın örneklerinin oluşturulması için kullanılan kurucu metoddur. Sınıfın özelliklerini (instance variable) tanımlamak ve başlatmak için kullanılır.
- `__str__(self)` : Bir nesneyi dizeye dönüştürmek için kullanılır. `str(obj)` gibi bir şekilde çağrılır. Örnek olarak, bir sınıftan türetilen bir nesnenin dize temsilini belirtmek için kullanılabilir.
- `__repr__(self)` : Bir nesneyi bir ifade olarak (representation) döndürmek için kullanılır. Örneğin, bir nesnenin tamamen yeniden oluşturulabilmesi için gerekli olan bilgileri içeren bir ifade döndürür.
- `__len__(self)` : Bir nesnenin uzunluğunu belirlemek için kullanılır. `len(obj)` gibi bir şekilde çağrılır.
- `__add__(self, other)` : İki nesneyi toplamak için kullanılır. `obj1 + obj2` gibi bir şekilde çağrılır.
- `__sub__(self, other)` : İki nesneyi çıkarmak için kullanılır. `obj1 - obj2` gibi bir şekilde çağrılır.
- `__mul__(self, other)` : İki nesneyi çarpmak için kullanılır. `obj1 * obj2` gibi bir şekilde çağrılır.
- `__div__(self, other)` : İki nesneyi bölerek bir nesne döndürmek için kullanılır. `obj1 / obj2` gibi bir şekilde çağrılır.
- `__eq__(self, other)` : İki nesnenin eşit olup olmadığını kontrol etmek için kullanılır. `obj1 == obj2` gibi bir şekilde çağrılır.
- `__lt__(self, other)` : Bir nesnenin diğer nesneden küçük olup olmadığını kontrol etmek için kullanılır. `obj1 < obj2` gibi bir şekilde çağrılır.

Bu sadece birkaç örnek, ama Python'da birçok özel metod bulunur. İhtiyaç duyduğunuz özel metodlara, sınıflarınıza ve projelerinize uygun olacak şekilde özelleştirerek kullanabilirsiniz.
"""