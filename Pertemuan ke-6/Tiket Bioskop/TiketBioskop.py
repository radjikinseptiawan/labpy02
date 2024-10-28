hargaTiketVIP = 100000
hargaTiketReguler = 50000
diskon = 20/100

pilhTiket = input("Pilih Tiket : (Reguler/VIP) ")



if pilhTiket.lower() == "reguler":
    isMember = input("Apakah kamu member : (Y/N) ")
    if isMember.upper() == "Y" :
        totalHarga = hargaTiketReguler * (1 - diskon)
        print(f'TOTAL HARGA : ',totalHarga)
    else : 
        print(f"TOTAL HARGA : ",hargaTiketReguler)
else : 
    isMemberTo = input("Apakah kamu member : (Y/N) ")
    if isMemberTo.upper() == "Y" :
        totalPrice = hargaTiketVIP * (1 - diskon)
        print(f'TOTAL HARGA : ',totalPrice)
    else : 
        print(f"TOTAL HARGA : ",hargaTiketVIP)
