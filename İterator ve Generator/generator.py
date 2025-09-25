def asal_sayi(bitis):
    for i in range(2, bitis):
        for j in range(2, i):
            if i % j == 0:
                break  # bölünebiliyorsa asal değil
        else:  # break olmadıysa
            yield i


bitiş = int(input("Hangi sayıya kadar almak istiyorsunuz: "))

for sayi in asal_sayi(bitiş):
    print(sayi)