rihatul = input('berat badan anda (kg)')
rekan = input('berat badan rekan anda (kg)')
rihatul = int(rihatul)
rekan = int(rekan)
hasil1 = rihatul - rekan
hasil2 = rekan - rihatul

if rihatul > rekan:
	kategori = 'anda lebih berat',int (hasil1),'kg dari rekan anda'

elif rekan > rihatul:
	kategori = 'anda lebih ringan',int(hasil2),'kg dari rekan anda'

else:
	kategori = 'berat badan anda sama dengan rekan anda'

print('{}'.format(kategori))
