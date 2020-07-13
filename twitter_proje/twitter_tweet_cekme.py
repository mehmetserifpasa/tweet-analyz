import requests
import json
import os
import sys
import re
import time
from src import cikti_yaz, Oranlari_yazdir
from matplotlib import pyplot as plt
from src.dik import Dik



class Analiz:

    def __init__(self):

        self.kufur = [kufur.strip() for kufur in open('src/listeler/kufur.txt')]
        self.kufur_oran = 0

        self.siyaset = [siyasi.strip() for siyasi in open('src/listeler/siyaset.txt')]
        self.siyaset_oran = 0

        self.olumlu = [olumlu.strip() for olumlu in open('src/listeler/olumlu.txt')]
        self.olumlu_oran = 0

        self.futbol = [futbol.strip() for futbol in open('src/listeler/futbol.txt')]
        self.futbol_oran = 0

        self.din = [din.strip() for din in open('src/listeler/din.txt')]
        self.dini_oran = 0

        self.olumsuz = [olumsuz.strip() for olumsuz in open('src/listeler/negatif.txt')]
        self.olumsuz_oran = 0


        self.kac_kez_gecti = set()
        self.kac_kez_gecti_list = []

        self.hicbirsey_bulunamayan_kelimeler = set()




    def kufur_liste(self, data, kufur_cumle):
        self.i = i
        self.kufur_cumle  = kufur_cumle

        if data in self.kufur:
            print("Argo içerikli: "+ data)

            self.kufur_oran += 1
            toplam_veri_kufur = ["Argo", data, self.i]
            cikti_yaz.Verileri_Yaz(toplam_veri_kufur)

        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



    def siyaset_liste(self, data, siyaset_cumle):
        self.siyaset_cumle = siyaset_cumle
        if data in self.siyaset:
            print("Siyaset içerikli cümle: "+ data)
            self.siyaset_oran += 1
            toplam_veri_siyaset = ["Siyaset", data, self.siyaset_cumle]
            cikti_yaz.Verileri_Yaz(toplam_veri_siyaset)
        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



    def olumlu_cumle(self, data, olum_cumle):
        self.olum_cumle = olum_cumle

        if data in self.olumlu:
            print("Pozitif içerikli: " + data)
            self.olumlu_oran += 1
            toplam_veri_olumlu = ["Olumlu", data, self.olum_cumle]
            cikti_yaz.Verileri_Yaz(toplam_veri_olumlu)

        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



    def futbol_liste(self, data, futbol_cumle):
        self.futbol_cumle = futbol_cumle

        if data in self.futbol:
            print("Futbol içerikli: " + data)
            self.futbol_oran += 1
            toplam_veri_futbol = ["Futbol", data, self.futbol_cumle]
            cikti_yaz.Verileri_Yaz(toplam_veri_futbol)

        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



    def din_liste(self, data, din_cumle):
        self.din_cumle = din_cumle

        if data in self.din:
            print("Dini içerik: "+ data)
            self.dini_oran += 1
            toplam_veri_din = ["Argo", data, self.din_cumle]
            cikti_yaz.Verileri_Yaz(toplam_veri_din)

        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



    def negatif_liste(self, data, negatif_cumle):
        self.negatif_cumle = negatif_cumle
        if data in self.olumsuz:
            print("Negatif içerikli cümle: "+ data)
            self.olumsuz_oran += 1
            toplam_veri_negatif = ["Argo", data, self.negatif_cumle]
            cikti_yaz.Verileri_Yaz(toplam_veri_negatif)

        else:
            self.hicbirsey_bulunamayan_kelimeler.add(data)



# ---------------------------------  TWEETLERİ ÇEKME BÖLÜMÜ  ---------------------------------

headers = {
    '' : ''
}


url = "https://api.twitter.com/2/timeline/profile/"+str(sys.argv[1])+".json?\
include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1\
&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1\
&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1\
&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&include_entities=true\
&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true\
&send_error_codes=true&simple_quoted_tweet=true&include_tweet_replies=true\
&userId="+str(sys.argv[1])+"&count=999999&ext=mediaStats%2ChighlightedLabel\
&include_quote_count=true"


istek = requests.get(url, headers=headers)
kaynak = istek.text
json_kaynak = json.loads(kaynak)
regex = json_kaynak['globalObjects']['tweets']
al = re.findall("'([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])'", str(regex))


tweetler = set() # sadece kendisinin attığı tweetler
tweetler_id = set()

rettweetler = set() # RT ler
rettweetler_id = set()

hepsi_karisik = set() # karısık id no
butun_Tweetler = set() # karışık


for k in al:

    hepsi_karisik.add(str(k))

for c in list(hepsi_karisik):

    try:

        tweet = json_kaynak['globalObjects']['tweets'][str(c)]['full_text']

        butun_Tweetler.add(json_kaynak['globalObjects']['tweets'][str(c)]['full_text'])

        if tweet[0] == "R" and tweet[1] == "T" and tweet[3] == "@":

            rettweetler.add(json_kaynak['globalObjects']['tweets'][str(c)]['full_text'])
            rettweetler_id.add(c)

        if tweet[0] != "R" and tweet[1] != "T" and tweet[3] != "@":

            tweetler.add(json_kaynak['globalObjects']['tweets'][str(c)]['full_text'])
            tweetler_id.add(c)

        continue

    except:

        pass




# --------------------------------- analiz bölümü ---------------------------------


obje = Analiz()
cc = 0


for i in butun_Tweetler: #sadece tweetleri görmek istiyorsak burayı düzenlemeliyiz
    cumlee = i.strip().split(" ")

    for k in cumlee:
        obje.kac_kez_gecti.add(k)
        obje.kac_kez_gecti_list.append(k)
        k = k.lower()

        obje.olumlu_cumle(k, i)
        obje.kufur_liste(k, i)
        obje.futbol_liste(k, i)
        obje.siyaset_liste(k, i)
        obje.din_liste(k, i)
        obje.negatif_liste(k, i)



oran_toplam = obje.olumlu_oran + obje.siyaset_oran + obje.kufur_oran + obje.dini_oran + obje.futbol_oran+ obje.olumsuz_oran


print("\n\n" + '-'*20 + " Tweet Analiz: " + str(len(butun_Tweetler))+" " + '-'*20
+"\nPozitif Oran: %" + str((int(obje.olumlu_oran)*100) / oran_toplam)[0:6]) #yüzde hesapladık ve ilk 5 karakterini bastırdık
print("Siyasi oran: %" + str((int(obje.siyaset_oran)*100) / oran_toplam)[0:6])
print("Argo oranı: %" + str((int(obje.kufur_oran)*100) / oran_toplam)[0:6])
print("Dini oran: %" + str((int(obje.dini_oran)*100) / oran_toplam)[0:6])
print("Futbol Oran: %" + str((int(obje.futbol_oran)*100) / oran_toplam)[0:6])
print("Negatif Oran: %" + str((int(obje.olumsuz_oran)*100) / oran_toplam)[0:6])


Oranlari_yazdir (
    kullanıcı_id = str(sys.argv[1]),
    pozitif = str((int(obje.olumlu_oran)*100) / oran_toplam)[0:6],
    siyasi = str((int(obje.siyaset_oran)*100) / oran_toplam)[0:6],
    argo = str((int(obje.kufur_oran)*100) / oran_toplam)[0:6],
    dini = str((int(obje.dini_oran)*100) / oran_toplam)[0:6],
    futbol = str((int(obje.futbol_oran)*100) / oran_toplam)[0:6],
    negatif = str((int(obje.olumsuz_oran)*100) / oran_toplam)[0:6]
)





# --------------------------------- KELİMELERİN KAÇ DEFA GEÇTİĞİNİ HESAPLAYAN SINIF ---------------------------------

print("\nLütfen Bekleyiniz...")


Dik().OranaGoreSiralama(
    pozitif=str((int(obje.olumlu_oran) * 100) / oran_toplam)[0:6],
    siyasi=str((int(obje.siyaset_oran) * 100) / oran_toplam)[0:6],
    argo=str((int(obje.kufur_oran) * 100) / oran_toplam)[0:6],
    dini=str((int(obje.dini_oran) * 100) / oran_toplam)[0:6],
    futbol=str((int(obje.futbol_oran) * 100) / oran_toplam)[0:6],
    negatif=str((int(obje.olumsuz_oran) * 100) / oran_toplam)[0:6]
)


#    geliştirilen bölüm








# ---------------------------------  SONUCA GÖRE PASTA GRAFİĞİ ÇİZİYORUZ ---------------------------------

fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #şekil ekseni
oran_adlari = ['Pozitif', 'Siyasi', 'Argo', 'Dini', 'Futbol', "Negatif"]
oran_renkleri = ["w", "b", "g", "r", "c", "m"] # Renkler, Kaynak: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html

oranlar = [str((int(obje.olumlu_oran)*100) / oran_toplam)[0:6],
            str((int(obje.siyaset_oran)*100) / oran_toplam)[0:6],
            str((int(obje.kufur_oran)*100) / oran_toplam)[0:6],
            str((int(obje.dini_oran)*100) / oran_toplam)[0:6],
            str((int(obje.futbol_oran)*100) / oran_toplam)[0:6],
            str((int(obje.olumsuz_oran)*100) / oran_toplam)[0:6],]

ax.pie( #pie pasta grafiği oluşturmamızı sağlar
        oranlar, # sayısal oranlar
        labels  = oran_adlari, # oran adları
        autopct = '%1.2f%%', #grafik içerisinde yüzde değerlerini gösterir
        #explode = (0,0,2,0,0,0)  istediğimiz oranın daha dışarıda olmasını sağlar
        #diğerleri 0 argoyu 2 kare dışarıda göster dedik
        #shadow=True ise gölge
      )

plt.title("Oran Çıktısı")
plt.show()


