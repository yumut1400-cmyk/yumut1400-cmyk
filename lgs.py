def net_hesapla(dogru, yanlis):
    return dogru - (yanlis / 3)

def lgs_puan_hesapla(turkce, matematik, fen, sosyal, yabanci, din):
    
	net_türkçe = net_hesapla(türkçe[0], türkçe[1])
    net_matematik = net_hesapla(matematik[0], matematik[1])
    net_fen = net_hesapla(fen[0], fen[1])
    net_sosyal = net_hesapla(sosyal[0], sosyal[1])
    net_yabanci = net_hesapla(yabanci[0], yabanci[1])
    net_din = net_hesapla(din[0], din[1])

    puan = (net_türkçe * 4) + (net_matematik * 4) + (net_fen * 4) + (net_sosyal * 1) +  (net_yabanci * 1) + (net_din * 1)

return puan

türkçe_doğru = float(input("Türkçe doğru sayısını giriniz: "))
türkçe_yanlış = float(input("Türkçe yanlış sayısını giriniz: "))

matematik_doğru = float(input("Matematik doğru sayısını giriniz: "))
matematik_yanlış = float(input("Matematik yanlış sayısını giriniz: "))

fen_doğru = float(input("Fen doğru sayısını giriniz: "))
fen_yanlış = float(input("Fen yanlış sayısını giriniz: "))

sosyal_doğru = float(input("Sosyal doğru sayısını giriniz: "))
sosyal_yanlış = float(input("Sosyal yanlış sayısını giriniz: "))

yabanci_doğru = float(input("Yabancı doğru sayısını giriniz: "))
yabanci_yanlış = float(input("Yabancı yanlış sayısını giriniz: "))

din_doğru = float(input("Din doğru sayısını giriniz: "))
din_yanlış = float(input("Din yanlış sayısını giriniz: "))

net_turkce = net_hesapla(turkce[0], turkce[1])
net_matematik = net_hesapla(matematik[0], matematik[1])
net_fen = net_hesapla(fen[0], fen[1])
net_sosyal = net_hesapla(sosyal[0], sosyal[1])
net_yabanci = net_hesapla(yabanci[0], yabanci[1])
net_din = net_hesapla(din[0], din[1])

print("NETLER")
print(f"Türkçe net: {net_türkçe:.2f}")
print(f"Matematik net: {net_matematik:.2f}")
print(f"Fen net: {net_fen:.2f}")
print(f"Sosyal net: {net_sosyal:.2f}")
print(f"Yabancı net: {net_yabanci:.2f}")
print(f"Din net: {net_din:.2f}")

puan = lgs_puan_hesapla((türkçe_doğru, türkçe_yanlış), (matematik_doğru, matematik_yanlış), (fen_doğru, fen_yanlış), (sosyal_doğru, sosyal_yanlış), (yabanci_doğru,yabanci_yanlış), (din_doğru, din_yanlış))

 print(f"LGS Puanınız: {puan:.2f}")