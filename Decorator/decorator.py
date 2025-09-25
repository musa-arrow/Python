def ekstra(func):
    def wrapper(list):
        for i  in list:
            toplam = 0
            for j in range(1,i):
                if i%j==0:
                    toplam += j
                else:
                    continue
            if i == toplam:
                    print(i)
        return func(list)
    return wrapper


@ ekstra
def yazdir(list):
    for i in list:
        print(i)

yazdir(range(1000))