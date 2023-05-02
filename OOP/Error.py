try:
    x = int(input("Bir sayı girin: "))
except ValueError:
    print("Hatalı giriş! Lütfen bir sayı girin.")


try:
    x = 10/0
except ZeroDivisionError:
    print("Sıfıra bölme hatası! Lütfen farklı bir sayı girin.")
