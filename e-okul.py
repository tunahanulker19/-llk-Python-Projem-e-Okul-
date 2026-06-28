import time

#Öğrenci İsimleri ve notları kümesi oluştur

öğrenci_ve_notlar = {}

#işlem menüsü

print("\nÖğrenci Notları Yönetim Sistemi")
while True:
    print("\n1. Öğrenci Ekle \n2. Not Ekle \n3. Notları Görüntüle \n4. Çıkış")
    işlem = int(input("\nBir işlem seçin (1-4): "))

    if işlem == 1:
        isim = input("Öğrencinin adlarını aralarına virgül koyarak girin: ")
        isimler = [i.strip() for i in isim.split(",")]
        for i in isimler:
            öğrenci_ve_notlar[i] = []
        print(f"{isimler} başarıyla eklendi.")

    elif işlem == 2:
        print("\nMevcut öğrenciler:")
        for i, isim in enumerate(öğrenci_ve_notlar.keys(), start=1):
            print(f"{i}. {isim}")

        secim = int(input("\nNot eklemek istediğiniz öğrencinin numarasını girin: "))
        if 1 <= secim <= len(öğrenci_ve_notlar):
            isim = list(öğrenci_ve_notlar.keys())[secim - 1]
            not_ekle = int(input(f"{isim} için notu girin: "))
            if 0 <= not_ekle <= 100:
                öğrenci_ve_notlar[isim].append(not_ekle)
                print(f"{secim} numaralı öğrencinin {not_ekle} notu başarıyla eklendi.")
            
            else:
                print("Geçersiz not. Lütfen 0-100 arasında bir not girin.")
        else:
            print(f"{secim} numaralı öğrenci bulunamadı.")
    
    elif işlem == 3:
        if not öğrenci_ve_notlar:
            print("\nHenüz öğrenci eklenmedi.")
        
        else:
             for isim, notlar in öğrenci_ve_notlar.items():
                print(f"\n {isim}: {notlar}")
    
    
    elif işlem == 4:
        print("Çıkış yapılıyor...")
        break

    elif işlem == 19:
        giris_metni = "\nBir japon atasözü der ki..."
        for harf in giris_metni:
            print(harf, end="", flush=True)
            time.sleep(0.06)

        time.sleep(2)
        print()

        bildirge_metni = "\nLa bu Honda Civic ne güzel arabaymış la göbel yeni kasa çok güzel olmuş heri \n-Hideki Tojo ve İmparator Jimmu Ahiret Ortak Bildirgesi"
        for harf in bildirge_metni:
            print(harf, end="", flush=True)
            time.sleep(0.05)  

        print("\n")
         
        break

    else:
        print("Geçersiz işlem. Lütfen 1-4 arasında bir sayı girin.")
