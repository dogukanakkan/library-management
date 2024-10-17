
class KitapView:
    @staticmethod
    def kitaplari_goster(kitaplar):
        if not kitaplar:
            print("\nHiç kitap yok.")
        else:
            print("\nKitap Listesi:")
            for i, kitap in enumerate(kitaplar, 1):
                odunc_durumu = "Ödünç Alındı" if kitap.odunc_alindi else "Müsait"
                print(f"{i}. {kitap.kitap_adi} - {kitap.yazar} - {kitap.sayfa_sayisi} sayfa - {kitap.kitap_turu} [{odunc_durumu}]")

    @staticmethod
    def kitap_ekle():
        kitap_adi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        sayfa_sayisi = int(input("Sayfa Sayısı: "))
        kitap_turu = input("Kitap Türü: ")
        return kitap_adi, yazar, sayfa_sayisi, kitap_turu

    @staticmethod
    def kitap_sec(kitaplar):
        KitapView.kitaplari_goster(kitaplar)
        try:
            secim = int(input("İşlem yapmak istediğiniz kitap numarasını girin: "))
            if 1 <= secim <= len(kitaplar):
                return secim - 1
            else:
                print("Geçersiz seçim.")
                return None
        except ValueError:
            print("Geçersiz seçim.")
            return None

    @staticmethod
    def kitap_guncelle():
        yeni_kitap_adi = input("Yeni Kitap Adı: ")
        yeni_yazar = input("Yeni Yazar: ")
        yeni_sayfa_sayisi = int(input("Yeni Sayfa Sayısı: "))
        yeni_kitap_turu = input("Yeni Kitap Türü: ")
        return yeni_kitap_adi, yeni_yazar, yeni_sayfa_sayisi, yeni_kitap_turu
