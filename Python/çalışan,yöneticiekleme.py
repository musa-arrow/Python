# class çalışan:
#     def __init__(self,isim,soyisim,maaş):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.maaş=maaş
#     def bilgileri_göster(self):
#         print("İsim : {}\nSoyisim : {}\nMaaş : {}\n".format(self.isim,self.soyisim,self.maaş))

# class yönetici(çalışan):
# #bu durumda direk aynısı gelir istersen eksta ekleyebilirsin.

class çalışan:
    def __init__(self,isim,soyisim,maaş):
        self.isim=isim
        self.soyisim=soyisim
        self.maaş=maaş
    def bilgileri_göster(self):
        print("İsim : {}\nSoyisim : {}\nMaaş : {}\n".format(self.isim,self.soyisim,self.maaş))

class yönetici(çalışan):
    def __init__(self, isim, soyisim, maaş,deparmant):
        super().__init__(isim, soyisim, maaş)
        self.departman=deparmant
    def bilgileri_göster(self):
        print("İsim : {}\nSoyisim : {}\nMaaş : {}\nDepartman : {}\n".format(self.isim,self.soyisim,self.maaş,self.departman))

yönetici1=yönetici("Musa","OK",300000,"Leader,CEO")

print(yönetici1.bilgileri_göster())
#bu durumda bir daha _init_ ve bilgileri gösteri tanımladığımız için ikiside iptal oldu kullanımda sonradan super fonkla istediğimiz bölümü çalışan fonkdan aldık.
#yani toplam 3 tane kalıtım, iptal etme ve super fonkla bir bölümünü alıoz.