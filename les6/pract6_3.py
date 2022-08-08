        # ЗАДАНИЕ №3
# Написать функцию перевода размеров женского белья из международного во все остальные. 
# Внутри функции нужно просто обращаться к правильно составленному словарю
size = {"XXS":{"germany":36, "usa":8, "france":38, "great britain":24}, 
"XS":{"germany":38, "usa":10, "france":40, "great britain":26},
"S":{"germany":40, "usa":12, "france":42, "great britain":28}, 
"M":{"germany":42, "usa":14, "france":44, "great britain":30}, 
"L":{"germany":44, "usa":16, "france":46, "great britain":32}, 
"XL":{"germany":48, "usa":18, "france":48, "great britain":34}, 
"XXL":{"germany":48, "usa":20, "france":50, "great britain":36}, 
"XXXL":{"germany":50, "usa":22, "france":52, "great britain":38}}

p = input("введите размер (" + " ".join(size) + "): ").upper()
b = input("Введите абривиатуру название страны, модельный ряд какой вы хотите получить(GE, USA, FR, или GB): ").lower()

def norm_size(s):
    
    for values in s[p]:
        if b == "ge":
            return s[p]["germany"]
        elif b == "usa":
            return s[p]["usa"]
        elif b == "fr":
            return s[p]["france"]
        elif b == "gb":
            return s[p]["great britain"]
        else:
            return "из перечня:\n" + str(s[p]).title()

print("Запрашиваемый размер", p, "будет равен размеру", norm_size(size))