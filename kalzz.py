#--------Tipe Data---------

#tipe data: Angka satuan (Integer)
data_integer=10
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#Tipe data float
data_float=10.5
print("Nilai data float >> ",data_float)
print("- bertipe", type(data_float))

#Tipe data String
data_String="mandalorian"
print("Tipe data String >> ", data_String)
print("- bertipe ",type(data_String))

#Tipe data boolean
data_bool=False
print("Tipe data boolean >> ", data_bool)
print("- bertipe ",type(data_bool))

## Tipe data Khusus

#Tipe data complex
data_complex=complex(5,6)
print("Tipe data complex >> ", data_complex)
print("- bertipe ", type(data_complex))

from ctypes import c_double

data_c_double=c_double(10.5)
print("Tipe data Double dari C >> ", data_c_double)
print("- bertipe ",type(data_c_double))
