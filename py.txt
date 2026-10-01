S1 = float(input("1. Snav Notunu Giriniz: "))
S2 = float(input("2. Snav Notunu Giriniz: "))
P1 = float(input("1. Performans Notunu Giriniz: "))

ort = (S1 + S2 + P1) / 3

if ort == 0:
    sonuc = "olumsuz"

elif ort >= 85:
    sonuc = "Pek iyi"

elif ort >= 70:
    sonuc = "Iyi"

elif ort >= 55:
    sonuc = "Orta"

elif ort >= 40:
    sonuc = "Gecer"

else:
    sonuc = "Basarısız"

print(f"Ortalama: {ort}")
print(f"Degerlendirme: {sonuc}")
