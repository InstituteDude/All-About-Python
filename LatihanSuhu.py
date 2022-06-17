# Latihan hitung sederhana menggunakan tempratur suhu

print("-> Latihan Tempratur Suhu F>K <-")

fahrenheit=float(input("Masukan suhu = "))
print("Suhu Fahrenheit >> ",fahrenheit,"Fahrenheit")

celcius=5/9*(fahrenheit-32)
print(" Suhu Celcius >> ",celcius,"Celcius")

reamur=4/9*(fahrenheit-32)
print("Suhu Reamur >> ",reamur,"Reamur")

kelvin=(5/9*(fahrenheit-32))+273
print("Suhu kelvin >> ",kelvin,"Kelvin")

print("-> Latihan Tempratur suhu K>F <-")

kelvin =float(input("Masukan Suhu = "))
print("Suhu Kelvin >> ",kelvin,"Kelvin")

celcius=kelvin-273
print("Suhu Kelvin ke Celcius >> ",celcius,"Celcius")

reamur=4/5*(kelvin-273)
print("Suhu Kelvin ke Reamur >> ",reamur,"Reamur")

fahrenheit=((kelvin-273.15)*9/5)+32
print("Suhu Kelvin ke Fahrenheit",fahrenheit,"Fahrenheit")
