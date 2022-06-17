# Operasi komparasi

# setiap hasil dari operasi Komparasi adalah boolean true/false

# >,<,>=,<=,==,!=,is,is not

print("-> lebih besar dari '>' <-")
a=5
b=7.1
hasil=a>6
print(a,">",3,"=",hasil)
hasil=b>5
print(b,">",5,"=",hasil)
hasil=7>b
print(7,">",b,"=",hasil)

print("-> Kurang dari '<' <- ")
a=6
b=9
hasil=a<7
print(a,"<",7,"=",hasil)
hasil=10<b
print(10,"<",b,"=",hasil)
hasil=a<b
print(a,"<",b,"=",hasil)

print("-> lebih dari sama dengan '>=' <-")
a=10
b=19
hasil=a>=b
print(a,">=",b,"=",hasil)
hasil=20>=b
print(20,">=",b,"=",hasil)
hasil=a>=10
print(a,">=",10,"=",hasil)

print("-> kurang dari sama dengan '<=' <-")
a=10
b=19
hasil=a<=b
print(a,"<=",b,"=",hasil)
hasil=20<=b
print(20,"<=",b,"=",hasil)
hasil=a<=10
print(a,"<=",10,"=",hasil)

print("-> sama dengan/membandingkan '==' <-")
a=10
b=19
hasil=a==b
print(a,"==",b,"=",hasil)
hasil=19==b
print(19,"==",b,"=",hasil)
hasil=a==10
print(a,"==",10,"=",hasil)

print("-> tidak sama dengan/membandingkan '!=' <-")
a=10
b=19
hasil=a!=b
print(a,"!=",b,"=",hasil)
hasil=19!=b
print(19,"!=",b,"=",hasil)
hasil=a!=10
print(a,"!=",10,"=",hasil)

# 'is' sebagai komparasi object identity
print("-> 'is' sebagai komparasi object identity <-")
x=5 #ini adalah assignment membuat object
y=5
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil=x is y
print('x is y = ',hasil)

print("-> 'is' sebagai komparasi object identity <-")
x=5 #ini adalah assignment membuat object
y=6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil=x is y
print('x is y = ',hasil)

print("-> 'is not' sebagai komparasi object identity tetapi mencari yang beda <-")
x=5 #ini adalah assignment membuat object
y=6
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil=x is not y
print('x is y = ',hasil)
