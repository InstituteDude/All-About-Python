# Operasi logika atau boolean

# Not, or, and, xor

print("====NOT====")
# Kebalikan dari semua boolean
a=True
c=not a
print(" data boolean =",a)
print(" data Boolean = ",c)

print("====OR====")
# Jika salah satu true, maka jawabannya akan true
a=False
b=False
c=a or b
print(a,'OR',b,'=',c)
a=True
b=False
c=a or b
print(a,'OR',b,'=',c)
a=True
b=True
c=a or b
print(a,'OR',b,'=',c)
a=False
b=False
c=a or b
print(a,'OR',b,'=',c)

print("====AND====")
# Operasi AND akan true apabila kedua nya true, 
# Bila salah satu atau atau tidak ada yang true maka akan menunjukan false
a=False
b=True
c=a and b
print(a,'AND',b,'=',c)
a=True
b=False
c= a and b
print(a,'AND',b,'=',c)
a=False
b=False
c=a and b
print(a,'AND',b,'=',c)
a=True
b=True
c=a and b
print(a,'AND',b,'=',c)

print('====XOR====')
# Operasi XOR akan true jila salah satu operasi bilangan true, tidak kedua bilangan nya
a=True
b=False
c=a ^ b
print(a,'XOR',b,'=',c)
a=False
b=True
c=a^b
print(a,'XOR',b,'=',c)
a=True
b=True
c=a^b
print(a,'XOR',b,'=',c)
a=False
b=False
c=a^b
print(a,'XOR',b,'=',c)
