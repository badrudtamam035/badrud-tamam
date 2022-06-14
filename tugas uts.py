menu={
    "Nasi Goreng"  :10.000,
    "Bakso Beranak":15.000,
    "Es Teh"       :7000,
    "Jus Buah"     :5000,
}
print("-------Daftar Menu------")
for i int menu:
        print("Daftar Menu:", i,"\t Harga:",menu[i])
print("Pembelian diatasi Rp100.000,-mendapatkan diskon 15%")  
print("====================================================")
beli=input("Pilih Menu:")
jumlah= int(input("Jumlah Pesanan:"))
bayar=jumlah * menu [beli]
  
if bayar >100000:
    diskon =bayar* 15/100
    total = bayar- diskon 
 
else :
      total = bayar
    
 print("---------Detail Pembayaran---------")
 print("Menu yang dipesan        :",beli)
 print("Jumlah yang dipesan      :",jumlah)
 print("Total Biaya              :",bayar)
 print("Total yang barus di bayar:",total)