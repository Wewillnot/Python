def ms(sayi):
    # Bulunan Sonuçların Ekleneceği Liste
    mükemmel_sayi = []
    # Bu Aralıktaki Mükemmel Sayıları Arıyoruz
    for i in range(1, sayi):
        # Tam Bölenleri Buluyoruz
        bölünensayilar = [sayi_ for sayi_ in range(1, i) if i%sayi_==0]
        bölenlertoplamı = sum(bölünensayilar)
        # Tam bölünenlerin toplamı girilen sayıya eşit mi kontrol ediyoruz
        if bölenlertoplamı == i:
            mükemmel_sayi.append(i)
    return mükemmel_sayi
