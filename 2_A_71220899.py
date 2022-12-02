def cetak_huruf(str):
    strLength=len(str)
    if strLength %2 == 0 :
        return str[0]+ str[1]+ str[2] + 'dan' + str [-3]+ str[-2]+ str[-1]
    else :
        tengah = int(strLength/2)
        return str[tengah-1]+ str[tengah]+ str[tengah+1]

kata=input("masukan kata:")
res= cetakhuruf(kata)
print("huruf yang diambil pada kata",kata,"adalah",res)