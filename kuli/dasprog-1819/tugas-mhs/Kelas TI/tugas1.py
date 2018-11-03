saya = input('Masukan berat badan anda (kg)')
rekan = input('Masukan berat badan rekan anda (kg)')
rekan = int(rekan)
saya = int(saya)
hasil1 = rekan - saya
hasil2 = saya - rekan

if rekan > saya:
	kategori = 'Anda lebih ringan',int (hasil1),'kg dari pada rekan anda'

elif saya > rekan:
	kategori = 'Anda lebih berat',int (hasil2),'kg dari pada rekan anda'

else:
	kategori = 'Berat badan anda sama dengan rekan anda'

print ('{}'.format(kategori))
