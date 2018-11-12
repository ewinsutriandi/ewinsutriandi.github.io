rifki = input('Masukan berat badan anda (kg)')
kami = input('Masukan berat badan rekan anda (kg)')
kami = int(kami)
rifki = int(rifki)
hasil1 = kami - rifki
hasil2 = rifki - kami

if rekan > saya:
	kategori = 'Anda lebih ringan',int (hasil1),'kg dari pada rekan anda'

elif saya > rekan:
	kategori = 'Anda lebih berat',int (hasil2),'kg dari pada rekan anda'

else:
	kategori = 'Berat badan anda sama dengan rekan anda'

print ('{}'.format(kategori))