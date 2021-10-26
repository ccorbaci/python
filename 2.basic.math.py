#NOTE : Toplama +
#NOTE : Çıkarma -
#NOTE : çarpma *
#NOTE : Bölme /
#NOTE : Üs **
#NOTE : Mod % - Bize kalanı verir örn 20. satır.
#NOTE : Tam Bölme //
#NOTE : İşlem önceliği her zaman parantez içlerindedir.

print(3+4)      #int
print(3.0+4)    #fload
print(3*5)      #int
print(3*4.1)    #fload
print(10/3)     #fload
print(10/5)     #fload - Yapmış olduğun bölme işleminin sonucu tam da olsa yine de fload olur.
print(3+5*2)    #int - çarpı operatörü artı operatörüne göre işlem önceliğine sahip.
print((3+5)*2)  #int - artı operatörü öncelikli olsun istiyosan bu şekilde yapmalısın.
print(3+5*6/2)  #fload - işin içine bölme girdiği için
print(2**3)     #int
print(10%3)     #int