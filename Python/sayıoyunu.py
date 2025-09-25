import random
import time

print("""*************************
             SAYI TAHMİN ETME OYUNU
      
      1 ile 40 arasında sayı söyle(1,40 dahil).
              
      
      ***********************""")

rastgelesayı=random.randint(1,40)#1 ile 40 dahil rastgele sayı üretir.
kaçta=1
puan=100
th=10
while True:
    sayı=int(input("Bir sayı girin : "))

    if(rastgelesayı==sayı):
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print(f"Tebrikler {kaçta}. seferde bildiniz.")
        print(f"Puanınız = {puan}")
        break

    elif(rastgelesayı>sayı):
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha büyük sayı girin.")
        kaçta+=1
        puan-=10
        th-=1
    
    else:
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha küçük sayı girin.")
        kaçta+=1
        puan-=10
        th-=1 

    if(th==0):
        print("Tahmin hakkınız bitti.")
        print(f"Sayınız = {rastgelesayı}")  
        break
    

    