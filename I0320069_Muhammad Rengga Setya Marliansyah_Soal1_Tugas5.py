kelamin1 = 'Tuan'
kelamin2 = 'Nyonya'
def lakilaki():
    nama = input('Masukan nama anda = ')
    print('Selamat datang,',kelamin1,nama,'!')
    mulai()
def perempuan():
    nama = input('Masukan nama anda = ')
    print('Selamat datang,',kelamin2,nama,'!')
    mulai()
def mulai():
    print('===== HOTEL MAWANG =====')
    print('Mohon isi biodata terlebih dahulu')
    print('1. Laki - laki')
    print('2. Perempuan')
    kelamin = input('Masukan jenis kelamin anda (1/2) = ')
    if kelamin == '1':
        lakilaki()
    elif kelamin == '2':
        perempuan()
    else:
        print('Input tidak valid')
        mulai()
mulai()


