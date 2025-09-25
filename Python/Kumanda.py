import random
import time

class kumanda:
    def __init__(self,durum="kapalı",tv_ses=0,kanal_list=["trt"],kanal="trt"):
        self.durum=durum
        self.tv_ses=tv_ses
        self.kanal_list=kanal_list
        self.kanal=kanal

    def tv_ac(self):
        if(self.durum=="açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.durum="açık"

    def tv_kapat(self): 
        if(self.durum=="kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...1")
            self.durum="kapalı"

    def ses_ayarları(self):

        while True:
            karar=input("Ses arttır : '>'\nSes azalt : '<'\n")
            if(karar=='<'):
                if(self.tv_ses!=0):
                    self.tv_ses-=1 
            elif(karar=='>'):
                if(self.tv_ses!=100):
                    self.tv_ses+=1
            else:
                print("Ses güncellendi...")
                break
    
    def ses_değiştirme(self):
        karar=int(input("Geçmek istedeğiniz ses seviyesi: "))
        self.tv_ses=karar

        print("Yeni ses seviyesi:",self.tv_ses)

    def kanal_ekleme(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_list.append(kanal_ismi)
    
    def kanal_silme(self,kanal_ismi):
        if kanal_ismi in self.kanal_list:
            print("Kanal siliniyor...")
            time.sleep(1)

            self.kanal_list.remove(kanal_ismi)#removede adının giriyon popda index i
        else:
            print("Kanal bulunamadı...")
            
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_list)-1)

        self.kanal=self.kanal_list[rastgele]
        
        print("Şu anki kanal :",self.kanal)
    
    def kanal_gecme(self):
        karar=input("Geçmek istediğiniz kanal ismi: ")
        self.kanal=karar

    def __len__(self):
        return len(self.kanal_list)
    
    def __str__(self):
        return "Tv durum: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.durum,self.tv_ses,self.kanal_list,self.kanal)
    
kumanda=kumanda()

print(""""
      
Televizyon uygulaması
      
1.Tv Aç
      
2.Tv Kapat

3.Ses Ayarları(Arttırma,azaltma)

4.Ses Değiştirme

5.Kanal Ekle
      
6.Kanal Silme

7.Kanal Sayısını Öğrenme

8.Kanal Değiştirme

9.Rastgele Kanala Geçme

10.Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")

while True:
    işlem=input("İşlemi seçiniz: ")

    if(işlem=='q'):
        print("Program sonlandı...")
        break

    elif(işlem=='1'):
        kumanda.tv_ac()
    
    elif(işlem=='2'):
        kumanda.tv_kapat()
    
    elif(işlem=='3'):
        kumanda.ses_ayarları()
    
    elif(işlem=='4'):
        kumanda.ses_değiştirme()

    elif(işlem=='5'):
        kanal_isimleri=input("Eklemek istediğiniz kanal isimleri(',' ile ayırın): ")
        kanal_listesi=kanal_isimleri.split(',')

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekleme(eklenecekler)
    
    elif(işlem=='6'):
        kanal_isimleri=input("Silmek istediğiniz kanal isimleri(',' ile ayırın): ")
        kanal_listesi=kanal_isimleri.split(',')

        for silenecekler in kanal_listesi:
            kumanda.kanal_silme(silenecekler)


    elif(işlem=='7'):
        print("Kanal sayısı: ",len(kumanda))#fonk adını(__len__) girmeden sadece len(adını) yazdığında len çağırılır
    
    elif(işlem=='8'):
        kumanda.kanal_gecme()

    elif(işlem=='9'):
        kumanda.rastgele_kanal()
    
    elif(işlem=='10'):
        print(kumanda)#fonk adını(__str__) girmeden sadece adını yazdığında str çağırılır
    
    else:
        print("Geçersiz işlem......\n")