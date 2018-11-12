#Kegiatan 2
pas = raw_input ("Masukkan Password :")

passaya = ("anisa")

w = 4
while w >= 0 :
    w = w - 1
    if 1 < w < 4 and pas != passaya :
        print ("Password anda salah.") ,
        pas = raw_input ("Masukkan password :")
    if w == 0 and pas != passaya :
        print ("Anda telah mencoba 3 kali. Akses anda di tolak")
    if 1 <= w <= 4 and pas == passaya :
        print ("Anda berhasil login.")
        break

        


#Kegiatan 3

nm = raw_input ("Masukkan Nama :")
pk = input ("Sekarang jam berapa?")
wkt = float (pk)

if 00.00 <= wkt <= 10.59 :
    print ("Selamat pagi" , nm)
elif 10.00 <= wkt <= 14.59 :
    print ("Selamat siang" , nm)
elif 14.00 <= wkt <= 18.59 :
    print ("Selamat sore" , nm)
elif 18.00 <= wkt <= 20.59 :
    print ("Selamat petang" , nm)
