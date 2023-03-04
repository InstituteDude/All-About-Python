# operator dalam bentuk methods

## merubah case dari string
# merubah semua ke upper case

salam = "homies!"
print("normal = " + salam)
salam = salam.upper()
print("upper = "+ salam)

# Merubah semua ke lower case
alay = "aKu KeCe AbiezzzzZzzZZ"
print("normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)


## pengecekan dengan isX method

# Contoh pengecekan lower case
salam = "SIST"
apakah_lower = salam.islower() # hasilnya bool
print(salam + "Is lower = "+ str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + "Is Upper = "+str(apakah_upper)) # hasilnya bool

# isalpha() <--- untuk mengecek bahwa semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi,tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = "+ str(cek_start))
cek_end = "Data".endswith("D")
print("end = "+ str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "surotong".ljust(10)
print("'"+kiri+"'")

tengah = "surotong".center(20,":")
print("'"+tengah+"'")

# kebalikannya -> strip()
kanan = kanan.strip(":") # menghilangkan tanda :
print("'"+kanan+"'")
