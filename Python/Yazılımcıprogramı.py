class yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller
    def bilgileri_göster(self):
        print("""
             Yazılımcının Özellikleri
             
              İsim : {}

              Soyisim : {}

              Numara : {}

              Maaş : {}

              Bildiği Diller : {}
 """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def maaş_zam(self,zammiktarı):
        print("Zam yapılıyor...")
        self.maaş+=zammiktarı

    def diller_ekle(self,ekledil):
        print("Dil ekleniyor...")
        self.diller.append(ekledil)

yazılımcı1=yazılımcı("Musa","OK",240309005,60000,["C","Python","Html","Css"])

print(yazılımcı1.bilgileri_göster(),end="\n")
yazılımcı1.maaş_zam(40000)
yazılımcı1.diller_ekle("C++")
print(yazılımcı1.bilgileri_göster())