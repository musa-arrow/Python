import requests
import sys
from datetime import datetime
import locale
import os
from dotenv import load_dotenv

try:
    locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
except:
    pass

load_dotenv()
api_key = os.getenv("OWM_API_KEY")

sehirler = {
    "adana": {"lat": 37.0000, "lon": 35.3213},
    "adıyaman": {"lat": 37.7648, "lon": 38.2786},
    "afyonkarahisar": {"lat": 38.7507, "lon": 30.5567},
    "afyon": {"lat": 38.7507, "lon": 30.5567},
    "ağrı": {"lat": 39.7191, "lon": 43.0503},
    "aksaray": {"lat": 38.3687, "lon": 34.0370},
    "amasya": {"lat": 40.6499, "lon": 35.8353},
    "ankara": {"lat": 39.9208, "lon": 32.8541},
    "antalya": {"lat": 36.8969, "lon": 30.7133},
    "ardahan": {"lat": 41.1105, "lon": 42.7022},
    "artvin": {"lat": 41.1828, "lon": 41.8183},
    "aydın": {"lat": 37.8560, "lon": 27.8416},
    "balıkesir": {"lat": 39.6484, "lon": 27.8826},
    "bartın": {"lat": 41.5811, "lon": 32.4610},
    "batman": {"lat": 37.8812, "lon": 41.1351},
    "bayburt": {"lat": 40.2552, "lon": 40.2249},
    "bilecik": {"lat": 40.0567, "lon": 30.0665},
    "bingöl": {"lat": 38.8845, "lon": 40.7696},
    "bitlis": {"lat": 38.4938, "lon": 42.1232},
    "bolu": {"lat": 40.5760, "lon": 31.5788},
    "burdur": {"lat": 37.7687, "lon": 30.2900},
    "bursa": {"lat": 40.1826, "lon": 29.0665},
    "çanakkale": {"lat": 40.1553, "lon": 26.4142},
    "çankırı": {"lat": 40.6013, "lon": 33.6134},
    "çorum": {"lat": 40.5506, "lon": 34.9556},
    "denizli": {"lat": 37.7765, "lon": 29.0864},
    "diyarbakır": {"lat": 37.9144, "lon": 40.2306},
    "düzce": {"lat": 40.8438, "lon": 31.1565},
    "edirne": {"lat": 41.6818, "lon": 26.5623},
    "elazığ": {"lat": 38.6810, "lon": 39.2264},
    "erzincan": {"lat": 39.7500, "lon": 39.5000},
    "erzurum": {"lat": 39.9000, "lon": 41.2700},
    "eskişehir": {"lat": 39.7767, "lon": 30.5206},
    "gaziantep": {"lat": 37.0662, "lon": 37.3833},
    "giresun": {"lat": 40.9128, "lon": 38.3895},
    "gümüşhane": {"lat": 40.4386, "lon": 39.5086},
    "hakkari": {"lat": 37.5833, "lon": 43.7333},
    "hatay": {"lat": 36.4018, "lon": 36.3498},
    "iğdır": {"lat": 39.8880, "lon": 44.0048},
    "isparta": {"lat": 37.7648, "lon": 30.5566},
    "istanbul": {"lat": 41.0082, "lon": 28.9784},
    "izmir": {"lat": 38.4192, "lon": 27.1287},
    "kahramanmaraş": {"lat": 37.5858, "lon": 36.9371},
    "karabük": {"lat": 41.2061, "lon": 32.6204},
    "karaman": {"lat": 37.1759, "lon": 33.2287},
    "kars": {"lat": 40.6013, "lon": 43.0975},
    "kastamonu": {"lat": 41.3887, "lon": 33.7827},
    "kayseri": {"lat": 38.7312, "lon": 35.4787},
    "kırıkkale": {"lat": 39.8468, "lon": 33.5153},
    "kırklareli": {"lat": 41.7333, "lon": 27.2167},
    "kırşehir": {"lat": 39.1425, "lon": 34.1709},
    "kilis": {"lat": 36.7184, "lon": 37.1212},
    "kocaeli": {"lat": 40.8533, "lon": 29.8815},
    "konya": {"lat": 37.8667, "lon": 32.4833},
    "kütahya": {"lat": 39.4167, "lon": 29.9833},
    "malatya": {"lat": 38.3552, "lon": 38.3095},
    "manisa": {"lat": 38.6191, "lon": 27.4289},
    "mardin": {"lat": 37.3212, "lon": 40.7245},
    "mersin": {"lat": 36.8000, "lon": 34.6333},
    "muğla": {"lat": 37.2153, "lon": 28.3636},
    "muş": {"lat": 38.9462, "lon": 41.7539},
    "nevşehir": {"lat": 38.6939, "lon": 34.6857},
    "niğde": {"lat": 37.9667, "lon": 34.6833},
    "ordu": {"lat": 40.9839, "lon": 37.8764},
    "osmaniye": {"lat": 37.2130, "lon": 36.1763},
    "rize": {"lat": 41.0201, "lon": 40.5234},
    "sakarya": {"lat": 40.6940, "lon": 30.4358},
    "samsun": {"lat": 41.2928, "lon": 36.3313},
    "siirt": {"lat": 37.9333, "lon": 41.9500},
    "sinop": {"lat": 42.0231, "lon": 35.1531},
    "sivas": {"lat": 39.7477, "lon": 37.0179},
    "şanlıurfa": {"lat": 37.1591, "lon": 38.7969},
    "şırnak": {"lat": 37.4187, "lon": 42.4918},
    "tekirdağ": {"lat": 40.9833, "lon": 27.5167},
    "tokat": {"lat": 40.3167, "lon": 36.5500},
    "trabzon": {"lat": 41.0015, "lon": 39.7178},
    "tunceli": {"lat": 39.5401, "lon": 39.4409},
    "uşak": {"lat": 38.6823, "lon": 29.4082},
    "van": {"lat": 38.4891, "lon": 43.4089},
    "yalova": {"lat": 40.6500, "lon": 29.2667},
    "yozgat": {"lat": 39.8181, "lon": 34.8147},
    "zonguldak": {"lat": 41.4564, "lon": 31.7987}
}


gun_isimleri = {
    "Monday": "Pazartesi",
    "Tuesday": "Salı",
    "Wednesday": "Çarşamba",
    "Thursday": "Perşembe",
    "Friday": "Cuma",
    "Saturday": "Cumartesi",
    "Sunday": "Pazar"
}


def hava_durumu_al(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.stderr.write(f"API bağlantı hatası: {e}\n")
        sys.stderr.flush()
        return None


def turkce_gun_getir(tarih_obj):
    ingilizce_gun = tarih_obj.strftime("%A")
    return gun_isimleri.get(ingilizce_gun, ingilizce_gun)


def hava_durumu_goster(data, gun_sayisi=5):
    if not data or data.get("cod") != "200":
        print("Hava durumu verisi alınamadı!")
        return

    print(f"\n🏙️ Şehir: {data['city']['name']}, {data['city']['country']}")
    print("=" * 60)

    gunluk_veriler = []
    for i in range(0, min(gun_sayisi * 8, len(data['list'])), 8):
        veri = data['list'][i]

        tarih = datetime.fromtimestamp(veri['dt'])
        turkce_gun = turkce_gun_getir(tarih)

        sicaklik = veri['main']['temp']
        hissedilen = veri['main']['feels_like']
        nem = veri['main']['humidity']
        durum = veri['weather'][0]['description']
        ruzgar = veri['wind']['speed']

        durum_turkce = {
            'clear sky': 'açık hava',
            'few clouds': 'az bulutlu',
            'scattered clouds': 'parçalı bulutlu',
            'broken clouds': 'çok bulutlu',
            'overcast clouds': 'kapalı',
            'light rain': 'hafif yağmur',
            'moderate rain': 'orta şiddetli yağmur',
            'heavy rain': 'şiddetli yağmur',
            'thunderstorm': 'gök gürültülü fırtına',
            'snow': 'kar',
            'mist': 'sisli'
        }.get(durum.lower(), durum.title())

        gunluk_veriler.append({
            'tarih': tarih.strftime("%d.%m.%Y"),
            'gun': turkce_gun,
            'sicaklik': sicaklik,
            'hissedilen': hissedilen,
            'nem': nem,
            'durum': durum_turkce,
            'ruzgar': ruzgar
        })

    for gun in gunluk_veriler:
        print(f"📅 {gun['tarih']} - {gun['gun']}")
        print(f"🌡️  Sıcaklık: {gun['sicaklik']:.1f}°C (Hissedilen: {gun['hissedilen']:.1f}°C)")
        print(f"☁️  Durum: {gun['durum'].title()}")
        print(f"💧 Nem: %{gun['nem']}")
        print(f"🌬️  Rüzgar: {gun['ruzgar']:.1f} m/s")
        print("-" * 40)


def main():
    try:
        print("🇹🇷 TÜRKİYE HAVA DURUMU UYGULAMASI 🇹🇷")
        print("=" * 50)
        print("Mevcut şehirler örneği: istanbul, ankara, izmir, antalya, trabzon...")
        print("(Türkiye'nin tüm 81 ili desteklenmektedir)")
        print()

        sehir = input("Hava durumunu öğrenmek istediğiniz şehri girin: ").lower().strip()

        try:
            gun_sayisi = int(input("Kaç günlük tahmin istiyorsunuz? (1-5): "))
            if gun_sayisi < 1 or gun_sayisi > 5:
                gun_sayisi = 5
                print("Varsayılan olarak 5 günlük tahmin gösteriliyor.")
        except ValueError:
            gun_sayisi = 5
            print("Geçersiz sayı! Varsayılan olarak 5 günlük tahmin gösteriliyor.")

        if sehir not in sehirler:
            sys.stderr.write("❌ Hata: Girdiğiniz şehir bulunamadı!\n")
            sys.stderr.write("Lütfen şehir adını doğru yazdığınızdan emin olun.\n")
            sys.stderr.write("Örnek: istanbul, ankara, izmir\n")
            sys.stderr.flush()
            return

        lat = sehirler[sehir]["lat"]
        lon = sehirler[sehir]["lon"]

        print(f"\n🔍 {sehir.title()} için hava durumu bilgileri alınıyor...")

        data = hava_durumu_al(lat, lon)

        if data:
            hava_durumu_goster(data, gun_sayisi)
        else:
            print("❌ Hava durumu verileri alınamadı!")

    except KeyboardInterrupt:
        print("\n\n👋 Program sonlandırıldı!")
    except Exception as e:
        sys.stderr.write(f"❌ Beklenmeyen hata: {e}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()