# list=[1,2,3,4,5]
# list.insert(1,"python")#1. index e python ı ekler.
# print(list)

# #bir şeyin neye yaradığını unuttuğunda help fonksiyonunu kullanabilirsin
# help(list.insert)

#--------------------------------------------------
# def birtoplama(sayı):
#     return sayı+1
# def ikiyleçarpma(sayı):
#     return sayı*2
# print(ikiyleçarpma(birtoplama(2)))
#--------------------------------------------------
# def selamla(isim="isimsiz",soyisim="soyisimsiz"):
#     print(f"isminiz : {isim} soyisminiz : {soyisim}")
# selamla("musa")
# selamla(soyisim="ok")#soyismine gireceksen ilk isim olduğu için böyle belirtmen lazım
# selamla()#İçine girilmdeiğinde default(varsayılan)değer girebilirsin böyle
#--------------------------------------------------
# print("09","01","2007",sep="/",end='\n')#normalde virgülde boşluğu değiştirmek için sep kullan istediğini koy. endlede sonunda ne girebileceğini belirtebilirsin.
#--------------------------------------------------
# def demetyapma(*a):
#     print(a)
# demetyapma(1,2,3) #istediğin kadar gir bunları demet şeklinde yazar.
#--------------------------------------------------
# def toplama(*a):
#     toplam=0
#     for i in a:
#         toplam+=i
#     print(toplam)

# toplama(1,2,3)
# toplama(1,2,3,4,5,6,7,8,9)
# #böyle bu özelliği kullanıp kullanıcının istediği kadar sayıyı yazıp işlem yapmayı sağlar.
#--------------------------------------------------
#Fonksiyonun içindeki değeri globsl yapmak için global x sonra x=5 mesela.
#--------------------------------------------------
# #fonksiyonları(tek işlemli) böyle tanımlayabilirsin
# ikiyleçarp = lambda x : x * 2
# print(ikiyleçarp(3))

# terscevir = lambda text : text[::-1]
# print(terscevir("Python"))
#---------------------------------------------------
# #modeüller import la dahil edilir
# import math #dosya ismi math
# #dirle modülde ne var bakılır
# dir(math)
# #help ne işe yaradıklarına bakılır
# help(math)
#-------------------------------------------------
# import math as matematik#böyle math modülünün ismini matematik yaptık
# matematik.factorial(5)
# matematik.floor(5.6)#kendisinden küçüğe yuvarlar
# matematik.ceil(5.6)#kendisinden büyüğe yuvarlar
# print(matematik.fabs(-5))#mutlak değeri alır
# #--------------------------------------------------
# from math import *#buda modül eklemenin diğer yolu * her elemanı yükle diye kullanıyoz sadece 1 2 tanesinide koyabilirsin(bunu kullanırsan fonk gibi eklediği için factorial yazıp sonra bunla eklersen senin yazdığını almaz en son yazılanı alır diğerinde böyle sorun yok.)
# factorial(5)#böyle eklersen tek tek ekleciğin için math.factorial(5) gibi yazmıyon
# #--------------------------------------------------
# from math import floor,ceil#sadece floorla ceili ekledin
# floor(3.9)
# #--------------------------------------------------
"""KENDİN MODÜL YAZIP EKLEMEK İSTERSEN YAZTIĞIN PYTHON DOSYAYALA AYNI KLASÖRDE OLMASI LAZIM
YA DA PYTHONUN MODÜLLERİNİN BULUBUĞU YERE ATMAN LAZIM O KLASÖRE"""
from itertools import count
from xml.sax.handler import feature_namespaces


#----------------------------------------------------
# class araba():
#     model_="C5 Aircross"
#     çıkışyılı_=2020
#     renk_="Kırmızı"
# araba1=araba()
# araba2=araba()

# print(araba1.model_)
# print(araba2.model_)
# print(araba.model_)
# #böyle ayrı ayrı değer giremioz.
# --------------------------------------------------
# class araba():
#     def __init__(self,model="Girilmemiş",çıkışyılı="Girilmemiş",renk="Girilmemiş"):
#         self.model_=model
#         self.çıkışyılı_=çıkışyılı
#         self.renk_=renk
# araba1=araba("C5",2020,"Kırmızı")#self i kendi kendine çağırıyor
# araba2=araba("C4",2019,"Mor")
# print(araba1.model_)
# print(araba2.model_)
#---------------------------------------------------------
class sonradankoyma():
    pass
#pythonda sonradan bişey koyacaksan pass yaz hata vermesin
#*******************************************************
# class bilgi:
#     def __init__(self,isim,soyisim,çalışmadurumu,sayfasayısı):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.çalışmadurumu=çalışmadurumu
#         self.sayfasayısı=sayfasayısı
#     def __str__(self):
#         return "isim : {}\nsoyisim : {}\nçalışmadurumu : {}\nsayfa sayısı : {}\n".format(self.isim,self.soyisim,self.çalışmadurumu,self.sayfasayısı)
#     def __len__(self):
#         return self.sayfasayısı
#     def __del__(self):
#         print("Person siliniyor...")
# person=bilgi("musa","ok","ÇALIŞIYOR",365)

# print(person.__str__())
# print(person.__len__())
# del person
# # print(person.__str__())#Hata verir çünkü person verisini siliyoruz.

# #DİĞER METODLARA SİTEDEN BAKABİLİRSİN.

# try:
#     print(int("c221"))
# except:
#     print("HATA")
# #exceptin yanına hata adları yazabilirsin sadece belirtebilirsin.

# def terscevir(x):
#     if(type(x)!=str):
#         print("Stringden başka bir şey girdin")#öyle hatanın altına sende ekleyebilirisn özelleştirebilrsin.
#     else:
#         return x[::-1]
# print(terscevir("Python"))
# print(terscevir(12))

# liste = ["345","sadas","324a","14","kemal"]

# # for i in liste:
# #     try:
# #         sayı=int(i)
# #         print(i,end='\n')
# #     except:
# #         print("Sayı değil\n")

# for i in liste:
#     try:
#         sayı=int(i)
#         print(i,end='\n')
#     except ValueError as e:#as e yle hata mesajını özelleştirebilrisin direk yanınas bişeyler yazabilrisin exceptin altındakiler hata mesajının altına yazılır raislede direk kendin hata mesajını yazıyon.
#         print("Hata: ",e)
        
# def çift(x):
#     if(x%2==0):
#         return x
#     else:
#         raise ValueError("Tek sayı  girdiniz:")#böylece hatayı direk sen yazabiliyon

# x=int(input("Sayı girin: "))
# print(çift(x))

#DOSYADA HER KARAKTER STRİNG OLDUĞU İÇİN SAYILARDA 1 BYTE KAPLAR YANİ HER KARKTER 1 BYTEDIR.

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","w",encoding="utf-8")#encoding utf 8 le html de ki gibi en geniş karakter dizisini kullanıyoz türkçe karakter desteği yani
# file.write("Yaren çok maldır.\n")
# file.write("BUT Musa çok akıllıdır.")
# file.close()

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r")
# for i in file:#Python bir işlemi bitirtikten sonra kendi kendine \n karakteri koyar önlemek için end="" kullan
#     print(i,end="")
# file.close()

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r")
# içerik=file.read()
# print(içerik)
# file.close()

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r")
# içerik=file.read()
# print(içerik)
# içerik2=file.read()
# print(içerik2)#Boş çıktı verir çünkü öncekinde okudu dosyanın sonuna geldi geldiği yerden okumaya başlar.
# file.close()

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r")
# print(file.readline())#tek satırı okur.
# file.close()

# file=open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r")
# liste=file.readlines()
# print(liste)#liste şeklinde yazdırılır.

#              DOSYAYI OTOMATİK KAPATMA (BÖYLE YAPTIĞINDA KENDİ KENDİNE DOSYAYI KAPATIYOR.)

#tell imlecin hangi byte da olduğunu söyler
#seek imleci istediğin byte yere götürebilirsin.
#read(10) gibi belirtirsen belirttiğin kadar byte okur.

"""
with open("C:\\Users\\DELL\\Desktop\\YAREN.txt","r+",encoding="utf-8",errors="ignore") as file:
    liste=file.readlines()
    print(liste)
    liste.insert(3,"PYTHON>ALL LEANGUES")
    file.seek(0)
    file.writelines(liste)# ya da for döngüsüyle okuyabilirsin."""
#-------------------------------------------------------------------------------------------------------
#map fonksiyonu içindekileri sırayla işleme sokar
#adres döndürür o yüzden list kullandık
def ikiyleÇarpma(x):
    return x*2
print(list(map(ikiyleÇarpma,(1,2,3,4,5))))

list1=[1,2,3,4,5,6]
list2=[0,0,0,0,0,0,2,3]
print(list(map(lambda x,y:x*y,list1,list2)))#list2 de dazla olan elemanları görmezden geliyor

#--------------------------------------------------------------------------------------------------------
#reduce fonksiyonunu eklemen lazım functools importundan çekmen lazım
#adres fonksiyonu sırayla işleme sokar aşağıda 1*2 sonra 2*3 sonra 6*4 sonra 24*5 120 bulunur.
from functools import reduce

print(reduce(lambda x,y:x*y,[1,2,3,4,5]))#faktöriyel alma 5'in

def maxNumber (x,y):
    if x>y:
        return x
    else:
        return y
print(reduce(maxNumber,[1,32,3,545,99,999,1000,0.3]))#max sayı bulma

#------------------------------------------------------------------------------------------------------
#filter reduce fonksiyonuyla aynı sadece true false döndürür.
#adres döndürür o yüzden list kullandık

print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9,10])))#çift olanları yazar

def asalNumber (x):
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        i=2
        while(i<x):
            if(x%2==0):
                return False
            i+=1
        return True
print(list(filter(asalNumber,range(1,101))))#asal sayı olanları yazar 1 den 100 e kadar 100 dahil

#--------------------------------------------------------------------------------------------------------------
#zip listeleri 2 li ,3 lü vb. şekilde gruplamımızı sağlar.
#adres döndürür o yüzden list kullandık
directionary1={"musa":1,"melike":2,"yaren":3}
directionary2={"ahmet":3,"mehmet":4,"furkan":5}
print(list(zip(directionary1,directionary2)))
print(list(zip(directionary1.values(),directionary2.values())))

listZip1=[1,2,3,4,5,6]
listZip2=["Python","Java","Html","Css","C","C++"]
for i,j in zip(listZip1,listZip2):
    print(i,":",j,end="\n",sep="-")

#--------------------------------------------------------------------------------------------------------------
#enumerate fonksiyonumuz (index,liste[index]) şeklinde yazar.
#adres döndürür o yüzden list kullandık.
listEnumerate1=["MUSA","OK","AREL"]
print(list(enumerate(listEnumerate1)))

#---------------------------------------------------------------------------------------------------------------
#all fonksiyonu hepsi true ise true,değilse false gönderir.
#any fonksiyonu 1 tane bile true varsa true,hepsi false ise false gönderir.

listeAllAndAny=[True,True,True,False]
print(all(listeAllAndAny))#False
print(any(listeAllAndAny))#True

#---------------------------------------------------------------------------------------------------------------
#ALIŞTIRMA GÖMÜLÜ FUNCTİONS
listÖdev=[(3,4),(10,3),(5,6),(1,9)]
print(list(map(lambda x : x[0] * x[1] ,(listÖdev))))

def üçgen (demet):
    a=abs(demet[0])
    b=abs(demet[1])
    c=abs(demet[2])

    if (a**2)+(b**2)==(c**2):
        return True
    else:
        return False
listÖdev2=[(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(üçgen,listÖdev2)))

listÖdev3=[1,2,3,4,5,6,7,8,9,10]
listÖdev4=list(filter(lambda x:x%2==0,listÖdev3))
print(reduce(lambda x,y:x+y,(listÖdev4)))

isimlerÖdev=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimlerÖdev=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(isimlerÖdev,soyisimlerÖdev):
    print(i,j)

#---------------------------------------------------------------------------------------------------------------
#SAYI FONKSİYONLARI
x=bin(4)#2 lik sayı sistemine çevirir.
print(x)

y=hex(16)#16 lığa çevirir.
print(y)

abs(-4)#mutlak değerini alır

z=round(5.6)#Yuvarlar alta yakınsa alta üste yakınsa üste yuvarlar.
c=round(5.2223,3)#virgülden sdonra kaç basamak istyon ona göre yuvarlıyor.

#Buna liste, demet vb.koyabilirsin yinede çalışır.
max(1,2,4,5)#max alır
min(1,2,4,5)#min alır.

sum([1,2,3,4.45,5])#toplamısını alır.(Sadece Demet ya da liste koyabilirsin.)

pow(12,2)#Üs alır.(12 nin karesini alır.)

#--------------------------------------------------------------------------------------------------------------
#STRİNG FONKSİYONLARI
print("python".upper())#harfleri büyütür
print("PYTHON".lower())#harfleri küçütür
print("musa".replace("a","o"))#harfleri yada kelimeleri farklı harfle değiştirebilirsiniz
print("Python programlama dili".replace(" ","-"))
print("Python".startswith("P"))# startswith : P yazdım mesela P ile başlıyorsa True başlamıyorsa False çıktısını verir
print("Python".endswith("on"))# endswith : aynı mantık neyle bittiğine bakıyor
benimBilgilerim="İstanbul Arel Üniversitesinde 1. sınıf Bilgisayar Mühendisliği okuyorum."
benimBilgilerimList=benimBilgilerim.split(" ")#içerisine göre listeye ayırır.(direk üstede yapabilirdim.)
print(benimBilgilerimList)

print("                     Pyhton                   ".strip())#Başdaki ve sondakileri siler ne yazarsan birşey yazmazsan Python yazar.
print("                     Pyhton                   ".lstrip())#aynı mantık sadece soldakileri siler
print("                     Pyhton                   ".rstrip())#aynı mantık sadece sağdakileri siler

stringList1=["09","01","2007"]
print("/".join(stringList1)) #Listeyi birleştirir ne yazarsan onla arasına koyar

stringList2=["T","B","M","M"]
print(".".join(stringList2))

print(benimBilgilerim.count("i"))#içindeki i yi sayar kaç tane var
print(benimBilgilerim.count("i",5))#ikinci değer hangi indexten başlayacağını belirtiyorsun istersen(5. indexte de dahil)

print(benimBilgilerim.find("b"))#içinde b varmı bakar(BAŞTAN)(yoksa -1 döndürür)(METİNDE YAZABİLİRSİN.)
print(benimBilgilerim.rfind("b"))#içinde b varmı bakar(SONDAN)(yoksa -1 döndürür)
print(benimBilgilerim.find("?"))

#------------------------------------------------------------------------------------------------------------------------------------
#KÜMELER
#KÜMELER SIRASIZDIR,
# HER ELEMAN TEK BİR TANE OLABİLİR(FAZLADAN YAZARSAN HATA VERMEZ AMA 1 TANE GİBİ ALIR.),
# SIRASIZ OLDLUĞU İÇİN İNDEXLE ULAŞAMAZSIN,KELİMEYLEDE ULAŞAMAZSIN.

#FOR DÖNGÜSÜYLE GEZİNEBİLİRSİN ÜSTÜNDE

küme1 = {1,2,3,4}

list3=["musa","ok"]
küme2=set(list3)#listeyi vb. şeyleri kümeye dönüştürme

#Kümeyi doğrudan yazdıramazsın.Listeye çevirebilirsin.
list4=küme1
for i in list4:
    print(i)
#KÜME FONKSİYONLARI
küme1.add(5)#eleman ekleme

küme3={1,2,3,4,5,6,7,8,9}
küme4={1,2,3}

küme5=küme3
küme6=küme4

print(küme3.difference(küme4))#küme3 ün küme4 den farkını yazar.
print(küme4.difference(küme3))#küme4 ün küme3 den farkını yazar.
#EĞER KÜME3 ÜN 4 DEN FARKINI ALIP ONU KÜME 3 E EŞİTLEMEK İSTİYORSAN:
küme3.difference_update(küme4)
print(küme3)

küme4.discard(2)#2 yi kaldırır (EĞER OLMAYAN DEĞERİ YAZSANDA HATA VERMEZ.)

küme3=küme5
küme4=küme6
print(küme3.intersection(küme4))#küme3 ile küme4 ün kesişimini yazarsın
#EĞER KESİŞİMİNİ KÜME3 E EŞİTLEMEK İSTİYORSAN:
küme3.intersection_update(küme4)
print(küme3)

print(küme3.isdisjoint(küme4))#eğer küme3 ile küme4 ün kesişimi varsa True , yoksa False döndürür.

print(küme3.issubset(küme4))#eğer 1.küme(küme3) 2.kümenin(küme4) ün alt kümesiyse True , değilse False döner.

print(küme3.union(küme4))#küme3 ile küme4 ün birleşimini alır.
#EĞER BİRLEŞİMİNİ ALIP KÜME3 E EŞİTLEMEK İSTİYORSAN:
küme3.update(küme4)
print(küme3)
#----------------------------------------------------------------------------------------------------------------------------------
#İLERİ SEVİYE LİSTE FONKSİYONLARI
#append,insert,pop,remove var
listL1=[1,2,3,4,5]
listL2=[10,20,30]
listL1.extend(listL2)#listL1 e listL2 ekliyon

print(listL1.index(4))#4 ün kaçıncı indexte olduğunu bulur.(BAŞTAN SONA BAKAR İLKİNİ SÖYLER.)
print(listL1.index(4,3))#4 ün kaçıncı indexte olduğunu 3. indexten itibaren arar.
print(listL1.count(2))#2 nin listede kaç tane olduğunu söyler.

listL1.sort()#sıralar sayıları küçükten büyüğe,harfleri alfebetik sıraya uygun şekilde sıralar.
listL1.sort(reverse=True)#Ters şekilde sıralanmasını sağlar.
print(listL1)

#----------------------------------------------------------------------------------------------------------------------------------
#SQLİTE VERİTABANI
import sqlite3

con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

tablo_olustur()
con.close()











