# app.py devamı
from controllers import KitapController


def menu():
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1. Kitapları Listele")
    print("2. Kitap Ekle")
    print("3. Kitap Güncelle")
    print("4. Kitap Sil")
    print("5. Kitap Ödünç Al")
    print("6. Kitap Geri Ver")
    print("7. Çıkış")
    return input("Bir seçenek girin: ")

def main():
    controller = KitapController()

    while True:
        secim = menu()
        if secim == "1":
            controller.kitaplari_listele()
        elif secim == "2":
            controller.kitap_ekle()
        elif secim == "3":
            controller.kitap_guncelle()
        elif secim == "4":
            controller.kitap_sil()
        elif secim == "5":
            controller.kitap_odunc_al()
        elif secim == "6":
            controller.kitap_geri_ver()
        elif secim == "7":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
