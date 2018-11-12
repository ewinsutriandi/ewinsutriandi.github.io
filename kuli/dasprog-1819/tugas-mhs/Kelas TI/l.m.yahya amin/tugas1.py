yahya = input('Masukan berat badan anda (kg)')
kita = input('Masukan berat badan rekan anda (kg)')
kita = int(kita)
yahya = int(yahya)
hasil1 = kita - yahya
hasil2 = yahya - kita

if kita > yahya:
	kategori = 'Anda lebih ringan',int (hasil1),'kg dari pada rekan anda'

elif yahya > kita:
	kategori = 'Anda lebih berat',int (hasil2),'kg dari pada rekan anda'

else:
	kategori = 'Berat badan anda sama dengan rekan anda'

print ('{}'.format(kategori))