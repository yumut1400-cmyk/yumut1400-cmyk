def net_hesapla(dogru, yanlis):
    return dogru - (yanlis / 3)

def ders_al(ders_adi, max_soru):
    while True:
        dogru = float(input(f"{ders_adi} doğru sayısını giriniz: "))
        yanlis = float(input(f"{ders_adi} yanlış sayısını giriniz: "))
        
        if 0 <= dogru <= max_soru and 0 <= yanlis <= max_soru and (dogru + yanlis) <= max_soru:
            return dogru, yanlis
        print(f"Hata! Değerler 0 ile {max_soru} arasında olmalı ve toplamları {max_soru}'yi geçmemelidir. Tekrar giriniz.")

def lgs_puan_hesapla(turkce, matematik, fen, sosyal, yabanci, din):
    net_turkce = net_hesapla(turkce[0], turkce[1])
    net_matematik = net_hesapla(matematik[0], matematik[1])
    net_fen = net_hesapla(fen[0], fen[1])
    net_sosyal = net_hesapla(sosyal[0], sosyal[1])
    net_yabanci = net_hesapla(yabanci[0], yabanci[1])
    net_din = net_hesapla(din[0], din[1])
                    
    netler = {
        "Türkçe": net_turkce,
        "Matematik": net_matematik,
        "Fen": net_fen,
        "Sosyal": net_sosyal,
        "Yabancı Dil": net_yabanci,
        "Din": net_din
    }
    
    puan = (net_turkce * 4) + (net_matematik * 4) + (net_fen * 4) + (net_sosyal * 1) + (net_yabanci * 1) + (net_din * 1) + 210
             
    return puan, netler

turkce = ders_al("Türkçe", 20)
matematik = ders_al("Matematik", 20)
fen = ders_al("Fen", 20)
sosyal = ders_al("Sosyal", 10)
yabanci = ders_al("Yabancı Dil", 10)
din = ders_al("Din", 10)

puan, hesaplanan_netler = lgs_puan_hesapla(turkce, matematik, fen, sosyal, yabanci, din)

print("\n--- NETLERİNİZ ---")
for ders, net in hesaplanan_netler.items():
    print(f"{ders} net: {net:.2f}")

print("\n------------------")
print(f"LGS Puanınız: {puan:.2f}")
