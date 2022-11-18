import math
panjang = int(input('Masukkan panjang:'))
lebar = int(input('Masukkan lebar: '))
jari = int(input('Masukkan jari-jari :'))
setlir = int((3.14*jari**2)/2)
ppanjang = int(panjang*lebar)
kaleng = (setlir+ppanjang)/15
print(f"Area tersebut Membutuhkan{math.ceil(kaleng)} kaleng cat")




