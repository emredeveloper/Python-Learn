class Meyve:
    cesit = 0

    def __init__(self, ad):
        self.ad = ad
        Meyve.cesit += 1

    @classmethod
    def bilgiVer(cls):
        print(f'{cls.cesit} çeşit meyve vardır!')


m1 = Meyve("Şeftali")
m2 = Meyve("Kayısı")
m3 = Meyve("Armut")

Meyve.bilgiVer()