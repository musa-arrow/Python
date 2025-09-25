import sys

sys.stderr.write("Bu bir hata mesajıdır\n") # Ekrana hata mesajı yazma
sys.stderr.flush() # Hata mesajını ekrana verdi

sys.stdout.write("Bu normal bir yazıdır\n") # Ekrana normal mesaj yazma

print(sys.argv)
'''
argv (argument values) komut satırından girilen değerleri bir liste olarak tutar.
Listenin ilk elemanı (sys.argv[0]) programın kendisidir, sonraki elemanlar ise program çalıştırılırken girilen argümanlardır.
'''

def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c

    if(delta < 0):
        print("Reel Kök Yok.")

    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("Lütfen doğru değerler girin.")
    sys.stderr.flush()

sys.exit() # Programı sonlandırır