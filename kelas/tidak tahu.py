# def perkenalan():


# def perkalian():
#     x = 5 * 3
#     print(x)

# perkalian()



# def perkenalan(parameter):
#     print(parameter)

# perkenalan('laras')



# def perkenalan(nama):
#     print(f'halo'{nama} selamat bergabung)
    
# perkenalan('laras')



# def LuasPersegiPanjang(panjang, lebar):
#     luas = panjang * lebar
#     print(f'luas dari Persegi Panjang adalah {luas}')

# LuasPersegiPanjang()



# def LuasPersegi(sisi):
#     Luas = sisi*sisi
#     return Luas

# #print('Luas Persegi : ', (LuasPersegi(8)))

# def volume_persegi(sisi):
#     volume = LuasPersegi(sisi) * sisi
#     print("Volume Persegi = ", volume)

# LuasPersegi(4)
# volume_persegi


# def faktorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# hasil = faktorial(8)
# print(f"Hasil dari 8! adalah: {hasil}")


# harga = int(input('masukan harga\t: '))
# print(harga)


# try :
#     angka = int(input('masukan harga\t: '))
# except ValueError:
#     print('inputan bukan berupa harga')
# else :
#     print(angka)
# finally :
#     print('laras 010')


# try :
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)
# else:
#     print(usn)

#studykasus
#Buatlah Error Handling untuk melakukan input nama dengan kriteria tidak boleh kosong atau hanya berisi spasi saja.
# try :
#     usn = input('masukan username : ')
#     if len(usn) < 0 or not usn.strip() == "":
#          raise ValueError('tidak boleh kosong')
# except ValueError as e:
#      print(e)
# else:
#      print(usn)


#
try :
     usn = input('masukan username : ')
     if len(usn) < 0 or not usn.strip() == "":
          raise ValueError('tidak boleh kosong')
except ValueError as e:
      print(e)
else:
      print(usn)
