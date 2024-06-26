def roman_to_arabic(roman):
    # Roma rakamlarının karşılıkları
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Geçerli Roma rakamı sıraları
    valid_subtractions = {
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    
    # Geçerli karakterler kontrolü
    for char in roman:
        if char not in roman_numerals:
            return "Geçersiz karakter bulundu: {}".format(char)

    # Geçerli Roma rakamı kurallarını kontrol etme
    def is_valid_roman(roman):
        import re
        pattern = "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        return bool(re.match(pattern, roman))
    
    if not is_valid_roman(roman):
        return "Geçersiz Roma rakamı formatı: {}".format(roman)

    i = 0
    num = 0
    while i < len(roman):
        # İki karakterli çıkarmaları kontrol et
        if i + 1 < len(roman) and roman[i:i + 2] in valid_subtractions:
            num += valid_subtractions[roman[i:i + 2]]
            i += 2
        else:
            num += roman_numerals[roman[i]]
            i += 1
    
    return num

# Kullanıcı girdisi alma ve sonucu gösterme
while True:
    roman_input = input("Roma rakamını girin (çıkmak için 'q' tuşlayın): ")
    if roman_input.lower() == 'q':
        break
    print("Sonuç:", roman_to_arabic(roman_input))
