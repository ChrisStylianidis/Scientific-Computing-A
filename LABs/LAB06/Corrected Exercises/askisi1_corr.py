#Askisi1 Christodoulos Stylianides
#!/bin/python3

string1="How"
string2="are you my friend"
int1=34
int2=942885
float1=-3.0
float2=3.14159265358979323846264E-14
print(string1)
print(string1+" "+string2)
print("A.{} {}".format(string1,string2))#me tin sira se kathe {} mpenei to kathena string
print("B.{0:s}{1:s}".format(string1,string2)) #to string 1 den exei space sto telos oute to string 2 stin arxi
print("C.{0:s}{0:s}{1:s}-{0:s}{1:s}".format(string1,string2))#apo to format tha parei dio fores to proto string kai meta tin pavla tha tiposei mono to proto kai deftero string
print("D.{0:10s}{1:5s}".format(string1,string2))#stin proti agkili tha tiposei 10 xaraktires tou protou string, dld ta 3 grammata how kai 7 kena
print("******")#diaxoristiko
print(int1,int2)
print("E.{0:d}{1:d}".format(int1,int2))#tiponei enomena ta 2 integers
print("F.{0:8d}{1:10}".format(int1,int2))#tiponei to proto int me 6 kena
print("G.{0:0.3f}".format(float1))#tiponei to float1 me 3 dekadika
print("H.{0:6.3f}".format(float1))#tiponei to float1 stin idia thesi me to G giati exei 6 xaraktires, simperilamvanomenon to plin kai to .
print("I.{0:8.3f}".format(float1))#dio space stin arxi giati einai 6 xaraktires to float 1
print(2*"J.{0:8.3f}".format(float1))#tiponei dio fores to I
print("******")
print("K.{0:0.3e}".format(float2))#me 3 dekadika to float2
print("L.{0:12.3e}".format(float2))#me keno 12-8=4 epd xrisimopiei 8 charaktires
print("M.{0:12.3f}".format(float2))#7 kena giati 12-5=7
print("******")
print("N. 12345678901234567890")#apla tiponei o,ti vlepei
print("O. {0:s}-{1:8d},{2:10.3e}".format(string2,int1,float2))#tiponei to proto string me mia pavla me 8-2=6 kena to int1 kai to float2 10-9=1 keno me 3 dekadika

exit()
#10/10