print("""***************************************

Atm makinesine hoşgeldiniz.

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basın.
*************************************************""")
1
bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")
    
    if işlem == "q":
        print("Yine bekleriz")
        break

    elif işlem == "1":
        print(f"Bakiyeniz {bakiye} TL'dir.")
    
    elif işlem == "2":
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        bakiye += miktar
        print(f"Güncel bakiyeniz {bakiye} TL'dir.")
    
    elif işlem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if bakiye - miktar < 0:
            print("Yetersiz bakiye.")
            continue  # Döngünün başına döner, aşağıdaki kodlar çalışmaz
        bakiye -= miktar
        print(f"Güncel bakiyeniz {bakiye} TL'dir.")

    else:
        print("Geçersiz işlem...")