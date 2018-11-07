saya = input('masukkan berat badan anda (Kg)')
rekan = input('masukkan berat badan rekan anda (Kg)')
rekan = int(rekan)
saya = int(saya)
hasil1 = (rekan - saya)
hasil2 = (saya - rekan)
if rekan>saya :
	kategori = 'anda lebih ringan', int (hasil1),'Kg dari rekan anda'
elif saya>rekan :
	kategori = 'anda lebih berat', int(hasil2),'Kg dasi rekan anda'
else :
	kategori = 'berat anda sama dengan rekan anda'
print('{}'.format(kategori))
	