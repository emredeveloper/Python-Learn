def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4
"""
Generators, Python'da dinamik olarak elemanlar üretmek için kullanılan fonksiyonlardır. 
Her çağrıldığında yeni bir eleman üreten ve durumunu hatırlayan bir fonksiyon olarak düşünebiliriz. 
Bu sayede bellekte gereksiz yere yer işgal etmeden, ihtiyaç duyulduğu anda elemanlar üretilebilir.
"""