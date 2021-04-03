def penghitungan():
    nama = input('Masukan nama anda = ')
    nilai =  int(input('Masukan nilai anda = '))
    if nilai < 60:
        print('Halo,',nama,'! Nilai anda setelah dikonversi adalah E')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 60 and nilai <= 64:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 65 and nilai <= 69:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C+')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 70 and nilai <= 74:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 75 and nilai <= 79:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B+')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 80 and nilai <= 84:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A-')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    elif nilai >= 85 and nilai <= 100:
        print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A')
        ulang = input('Coba lagi? (y/t) = ')
        if ulang == 'y':
            mulai()
        elif ulang == 't':
            print('Terima kasih telah menggunakan Program Grading Nilai!')
    else:
        print('Masukan angka 0 - 100!')
        penghitungan()
def mulai():
    print('===== Program Grading Nilai =====')
    penghitungan()
mulai()

