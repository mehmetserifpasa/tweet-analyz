__author__ = "@d3r3li"
# Dil İşleme Kütüphanesi

import requests
import json
import os
import sys
import re
import time


class Dik:

    def __init__(self):
        self.title = ""




    def VeriLen(self, cumle):     # verilen cümlede kaç tane kelime olduğunu sayı cinsinden geri döndürür

        self.cumle = cumle
        veri_say = 0

        try:

            return len(self.cumle)
        except:

            print("Kelime genişliği hatası !")



    def OranaGoreSiralama(self, **kwargs):

        # Bu fonksiyon en fazla oranı bulunan 3 kategoriyi gösterir

        self.max_Oran = ["", 0]
        self.max_Say = 0
        self.Oran_Liste = []


        for OranAd, Oran in kwargs.items():

            Temiz_Oran = round(float(Oran))










"""            if int(Temiz_Oran) > self.max_Oran[1]:

                self.max_Oran[0] = OranAd
                self.max_Oran[1] = int(Temiz_Oran)"""










