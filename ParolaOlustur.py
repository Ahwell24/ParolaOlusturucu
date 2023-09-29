import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
prluzunluk = int(input("Parolanızın kaç karakterden oluşmaşını istiyorsununz ???"))
sifre = ""

for i in range(prluzunluk):
    sifre += random.choice(karakterler)
    
print(sifre)
