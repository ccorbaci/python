#NOTE : Değişkenler.Geçici olarak bir veri sakladığımız alana deniyor en kaba tabirle.

#NOTE : Örnek olarak 5000 tl lik bir ürün alıyorsak KDV ile beraber hesaplatacağımızı varsayarsak;

print((5000)+(5000*0.18)) #Ödeyecek olduğumuz fiyatı buluruz.
print((6000)+(6000*0.18)) #Başka bir ürün daha aldığımızı varsayalım. Her seferinde bu şekilde kod yazmamız gerek.

#NOTE : 2 tane ürün için sıkıntı yok fakat 200 300 üründe ne olacak? Şu şekilde yapacağız.

urunA = 6000
urunB = 7000
urunC = 8000
kdv = 0.18

print(urunA + (urunA*kdv))
print(urunB + (urunB*kdv))
print(urunC + (urunC+kdv))

#NOTE : Değişken tanımlama kuralları;
#NOTE : Rakam ile başlayamaz.Alfanumerik karakteler ile başlayamaz.
#NOTE : Arada boşluk olamaz. Alt çizgi eklenebilir. - de eklenemez.
#NOTE : Büyük küçük harf duyarlığı var.Büyük ve küçük harfler farklı değişkenler tanımlar.
#NOTE : a , b , c gibi tek seferde bir çok değişken tanımlanabilir.

a, b, c = 10, 20, 30
print(a + b + c)

#NOTE : Daha sonra değinilecek ama not olarak ;

"""
x = 1              # int
y = 2.3            # float 
name = "Çınar"     # string
isStudent = True   # bool

string olarak " " arasına yazınca
a = "10"
b = "20"
print(a+b) # => 1020

firstName = "Sadık"
lastName = " Turan"

print(firstName + lastName)  # Sadık Turan

"""
