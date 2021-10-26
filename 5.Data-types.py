#int
#float
#string
#bool

#NOTE : bu şekilde int olarak yazarak matematiksel işlemler yaparız buraya kadar tamam.

"""
x =10
y =20
toplam = x + y
print(toplam)

"""

#NOTE : bu şekilde de string olarak tanımlayıp yan yana da yazdırabiliriz buraya kadar da tamam.

"""
x ="10"
y ="20"
toplam = x + y
print(toplam)

"""

#NOTE : Peki int toplam olarak yazdıracaksak.O zaman da şöyle yapıyoruz.

"""
x =10
y =20
toplam = x + y
print(toplam)

"""

#NOTE : Peki bu değerleri biz kullanıcıdan alacaksak ve string olarak yazdıracaksak. O zaman da şu şekilde yapılır.

"""
adi =input("Adınız: ")
soyadi =input("Soyadınız: ")
adısoyadi = adi +" "+ soyadi
print(adısoyadi)

"""

#NOTE : type bilgisini de bu şekilde okutabiliriz hatta.

"""

x= input("x: ")
y= input("y: ")

print(type(x))
print(type(y))

toplam = x + y 
print(toplam)

"""

#NOTE : Type bilgisi olarak kullanıcıdan aldığımız değeri dönüştürmemiz gerek.int komutu değeri inte çevirerek matematiksel işlem yapar.

"""
x= int(input("x "))
y= int(input("y "))

print(type(x))
print(type(y))

toplam = x + y 
print(toplam)

"""


age = 5
weight = 7.5
name = "Cüneyt"
isStudent = True

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))

#NOTE : int türündeki bir değeri float türüne çevirmek istersem

result = float(age)
print(type(result))
print(result)

#NOTE : Float türündeki bir değeri int türüne çevirmek istersek

result = int(weight)
print(type(result))
print(result)

# NOTE : bool türünden str türüne çevirmek istersek

result = str(isStudent)
print(type(result))
print(result)