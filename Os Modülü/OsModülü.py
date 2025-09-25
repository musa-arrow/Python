import os
from datetime import datetime

os.chdir("C:/Users/DELL/Desktop") # os modülünün yerini değiştirme
print(os.getcwd()) # os modülünün nerde olduğunu gösterir

# print(os.listdir()) # os modülünün olduğu yerdeki klasörleri ve dosyaları gösterir
for i in os.listdir():
    print(i)

os.mkdir("Deneme1") # os modülünün olduğu yere Deneme1 adında klasör oluşturur (KLASÖR)
os.makedirs("Deneme2/Deneme3") # os modülünün olduğu yere Deneme2 , Deneme2' nin altına Deneme3 adlı klasörleri oluşturur (KLASÖR)

if not os.path.exists("Deneme1"): # Böyle yoksa oluştur diyebilirsin
    os.mkdir("Deneme1")
else:
    print("Klasör zaten var!")

os.rmdir("Deneme2/Deneme3") # Deneme3 klasörünü siler (KLASÖR)
os.makedirs("Deneme2/Deneme3")
os.removedirs("Deneme2/Deneme3") # Deneme2 ve Deneme3 klasörünü siler (KLASÖR)

os.rename("test.txt","test2.txt") # os modülünün olduğu yerdeki test.txt yi test2.txt yapar (DOSYA ve KLASÖR)

print(os.stat("test2.txt")) # test2.txt ' nin bütün özelliklerini verir (DOSYA ve KLASÖR)

print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) # st_mtime -> değiştirilme zamanı , gibi özelliklerini alabilirsin bu şekilde (DOSYA ve KLASÖR)

for i in os.walk("C:/Users/DELL/Desktop"): # Bu yolun altındaki bütün dosyaları ve klasörleri gösterir
    print(i)

for klasör_yolu,klasör_isimleri,dosya_isimler in os.walk("C:/Users/DELL/Desktop"):
    print("Klasör Yolu",klasör_yolu)
    print("Klasör İsimleri", klasör_isimleri)
    print("Dosya İsimleri", dosya_isimler)
    print("******************************************")

for klasör_yolu,klasör_isimleri,dosya_isimler in os.walk("C:/Users/DELL/Desktop"):
    for i in dosya_isimler:
        if(i.endswith(".txt")): # sadece txt dosyalarını alır
            print(i)