# controllers.py
from models import KitapModel
from views import KitapView

class KitapController:
    def __init__(self):
        self.model = KitapModel()

    def kitaplari_listele(self):
        KitapView.kitaplari_goster(self.model.kitaplar)

    def kitap_ekle(self):
        kitap_adi, yazar, sayfa_sayisi, kitap_turu = KitapView.kitap_ekle()
        self.model.kitap_ekle(kitap_adi, yazar, sayfa_sayisi, kitap_turu)
        print(f"'{kitap_adi}' kitabı eklendi.")

    def kitap_guncelle(self):
        secilen_index = KitapView.kitap_sec(self.model.kitaplar)
        if secilen_index is not None:
            yeni_kitap_adi, yeni_yazar, yeni_sayfa_sayisi, yeni_kitap_turu = KitapView.kitap_guncelle()
            self.model.kitap_guncelle(secilen_index, yeni_kitap_adi, yeni_yazar, yeni_sayfa_sayisi, yeni_kitap_turu)
            print("Kitap bilgileri güncellendi.")

    def kitap_sil(self):
        secilen_index = KitapView.kitap_sec(self.model.kitaplar)
        if secilen_index is not None:
            self.model.kitap_sil(secilen_index)
            print("Kitap silindi.")

    def kitap_odunc_al(self):
        secilen_index = KitapView.kitap_sec(self.model.kitaplar)
        if secilen_index is not None:
            if self.model.kitap_odunc_al(secilen_index):
                print("Kitap ödünç alındı.")
            else:
                print("Kitap zaten ödünç alınmış.")

    def kitap_geri_ver(self):
        secilen_index = KitapView.kitap_sec(self.model.kitaplar)
        if secilen_index is not None:
            if self.model.kitap_geri_ver(secilen_index):
                print("Kitap geri verildi.")
            else:
                print("Kitap zaten kütüphanede.")
