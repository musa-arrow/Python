import os

baslangic_dizini = "C:\\"


pdf_dosyasi = "pdf_dosyalari.txt"
mp4_dosyasi = "mp4_dosyalari.txt"
txt_dosyasi = "txt_dosyalari.txt"


open(pdf_dosyasi, "w", encoding="utf-8").close()
open(mp4_dosyasi, "w", encoding="utf-8").close()
open(txt_dosyasi, "w", encoding="utf-8").close()

for klasor_yolu, alt_klasorler, dosyalar in os.walk(baslangic_dizini):
    for dosya in dosyalar:
        dosya_yolu = os.path.join(klasor_yolu, dosya)

        if dosya.lower().endswith(".pdf"):
            with open(pdf_dosyasi, "a", encoding="utf-8") as f:
                f.write(dosya_yolu + "\n")

        elif dosya.lower().endswith(".mp4"):
            with open(mp4_dosyasi, "a", encoding="utf-8") as f:
                f.write(dosya_yolu + "\n")

        elif dosya.lower().endswith(".txt"):
            with open(txt_dosyasi, "a", encoding="utf-8") as f:
                f.write(dosya_yolu + "\n")

print("✅ İşlem tamamlandı. Sonuçlar txt dosyalarına kaydedildi.")
