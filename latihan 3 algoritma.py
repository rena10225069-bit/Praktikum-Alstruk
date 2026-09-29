#Memasukkan bilangan
bilangan = int(input("Masukkan bilangan:"))
#Bilangan prima harus lebih besar dari 1
if bilangan > 1:
    is_prima = True
    #Mengecek faktor pembagi dari 2 hingga (bilangan - 1)
    for i in range(2, bilangan):
        if(bilangan % i) == 0:
            is_prima = False
            break

#Menampilkan hasil
if is_prima:
    print("Bilangan prima")
else:
    print("Bukan bilangan Prima")