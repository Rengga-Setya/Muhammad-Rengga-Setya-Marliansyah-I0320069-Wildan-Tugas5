#penggunaan if untuk tiga kasus
#inputkan bilangan
print('Masukan kordinat!')
x = int(input('Masukan nilai x : '))
y = int(input('Masukan nilai y : '))
info = 'koordinat (' + str(x) + ',' + str(y) + ') berada pada kuadran '
#memeriksa nilai x dan y
if x > 0 and y > 0:
	print(info + 'I')
elif x< 0 and y > 0:
	print(info + 'II')
elif x < 0 and y < 0:
	print(info + 'IV')
else:
	pass
print()
