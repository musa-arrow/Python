def asalsayı(x):
    if(x==1):
        return False
    elif (x==0):
        return False
    else:
        for i in range(2,x):
            if(x%i==0):
                return False
        return True

while True:
    sayı=input("(çıkmak için q ya bas.)\nSayı : ")

    if(sayı=='q'):
        print("İşleminiz bitti....")
        break
    else:
        sayı=int(sayı)
        if (asalsayı(sayı)):
            print(sayı,"asal sayı")
        else:
            print(sayı,"asal sayı değil")

