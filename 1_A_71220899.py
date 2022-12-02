print("======= Program Manipulasi String =======")
print("pilihan Menu")
print("1.Hitung kata")
print("2.ubah kata")
inputan = int(input ("pilihan anda:"))
kata=input("masukan sebuah kalimat/kata:")
def hitung_kata():
    a=input("masukan sebuah kalimat yang ingin dihitung")
    Fa=kata.count(a)
    print("terdapat sebanyak",Fa,"kata",a,"di dalam kalimat")
def ubah_kata():
    b=input("masukan kata yng ingin diubah:")
    fb=input("masukan kata pengganti:")
    c=kata.replace(b,fb)
    print("string beirhasil diubah menjadi :",c)
if pilihan=="1":
    hitung_kata()
elif pilihan=="2":
    ubah_kata ()
else:
    print("pilihan yang anda input tidak terdaftar di daftar pilihan")



