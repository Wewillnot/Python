import math
import time
import mükemmelsayi # mükemmelsayi modülünü ekliyoruz.

while True:
    gir = input("""
-----------------------------
Hesap Makinesi:
1-)Kök Alma
2-)Faktöriyel
3-)Mukemmel Sayı
4-)Euler Sabiti Kuvveti
Çıkmak İçin "q" Değerini Girin
------------------------------
İşlem:""")

    if gir is "q":
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        break

    elif gir is "1":
        us = int(input("Sayıyı Giriniz:"))
        time.sleep(1)
        print("Sonuç:",math.sqrt(us))

    elif gir is "2":
        fac = int(input("Sayıyı Giriniz:"))
        time.sleep(1)
        print("Sonuç:",math.factorial(fac))

    elif gir is "3":
        sayi = int(input("Hangi aralıktaki mükemmel sayılar hesaplansın ? Örn:(1,1000)\nİşlem:1,"))
        time.sleep(1)
        print("Sonuç:",mükemmelsayi.ms(sayi))
        
    elif gir is "4":
      eul = int(input("Sayıyı Giriniz:"))
      time.sleep(1)
      print("Sonuç:",math.exp(eul))
    
    else:
      print("Lütfen 4 Seçenekten Birini Giriniz")
      continue
