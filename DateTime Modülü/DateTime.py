from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

su_an = datetime.now()
print(su_an.year)
print(su_an.month)
print(su_an.hour)
print(datetime.ctime(su_an))
print(datetime.strftime(su_an,"%Y"))
print(datetime.strftime(su_an,"%B"))
print(datetime.strftime(su_an,"%D"))
print(datetime.strftime(su_an,"%A"))
print(datetime.strftime(su_an,"%B %Y"))

saniye = datetime.timestamp(su_an)# Tarihi saniye olarak gösterir (1970-01-1 den itibaren)
print(saniye)

su_an2 = datetime.fromtimestamp(saniye)# Saniye şeklindeki tarihi normale çevirir
print(su_an2)

tarih = datetime(2019,12,1)
su_an = datetime.now()
print(su_an - tarih)
