saya = input ('masukan berat badan anda (kg) ')
rekan = input ('masukan berat badan rekan anda (kg) ')
saya = int(saya)
rekan = int(rekan)
hasil1 = (rekan - saya)
hasil2 = (saya - rekan)

if rekan>saya :
	kategori = 'berat badan anda lebih ringan', int(hasil1), 'kg dari rekan anda'
elif saya>rekan :
	kategori = 'berat badan anda lebih berat', int(hasil2), 'kg dari rekan anda'
else :
	kategori = 'berat badan anda sama dengan rekan anda'
print('{}'. format(kategori))