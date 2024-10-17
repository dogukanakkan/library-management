import os

class Kitap:
    def __init__(self, kitap_adi, yazar, sayfa_sayisi, kitap_turu):
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.kitap_turu = kitap_turu
        self.odunc_alindi = False

class KitapModel:
    def __init__(self, dosya_adi="kitaplar.txt"):
        self.dosya_adi = dosya_adi
        self.kitaplar = self.kitaplari_yukle()

    def kitaplari_yukle(self):
        kitaplar = []
        if os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, 'r') as file:
                for line in file:
                    kitap_adi, yazar, sayfa_sayisi, kitap_turu, odunc_alindi = line.strip().split('---')
                    kitap = Kitap(kitap_adi, yazar, int(sayfa_sayisi), kitap_turu)
                    kitap.odunc_alindi = odunc_alindi == "True"
                    kitaplar.append(kitap)
        return kitaplar

    def kitaplari_kaydet(self):
        with open(self.dosya_adi, 'w') as file:
            for kitap in self.kitaplar:
                file.write(f"{kitap.kitap_adi}---{kitap.yazar}---{kitap.sayfa_sayisi}---{kitap.kitap_turu}---{kitap.odunc_alindi}\n")

    def kitap_ekle(self, kitap_adi, yazar, sayfa_sayisi, kitap_turu):
        yeni_kitap = Kitap(kitap_adi, yazar, sayfa_sayisi, kitap_turu)
        self.kitaplar.append(yeni_kitap)
        self.kitaplari_kaydet()

    def kitap_sil(self, index):
        del self.kitaplar[index]
        self.kitaplari_kaydet()

    def kitap_guncelle(self, index, yeni_kitap_adi, yeni_yazar, yeni_sayfa_sayisi, yeni_kitap_turu):
        self.kitaplar[index].kitap_adi = yeni_kitap_adi
        self.kitaplar[index].yazar = yeni_yazar
        self.kitaplar[index].sayfa_sayisi = yeni_sayfa_sayisi
        self.kitaplar[index].kitap_turu = yeni_kitap_turu
        self.kitaplari_kaydet()

    def kitap_odunc_al(self, index):
        if not self.kitaplar[index].odunc_alindi:
            self.kitaplar[index].odunc_alindi = True
            self.kitaplari_kaydet()
            return True
        return False

    def kitap_geri_ver(self, index):
        if self.kitaplar[index].odunc_alindi:
            self.kitaplar[index].odunc_alindi = False
            self.kitaplari_kaydet()
            return True
        return False
