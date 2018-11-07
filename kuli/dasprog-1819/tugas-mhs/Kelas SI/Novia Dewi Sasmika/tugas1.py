saya = input('Masukkan berat badan anda {kg}')
rekan = input('Masukkan berat badan rekan anda {kg}')
rekan = int(rekan)
saya = int(saya)
hasil1 = rekan - saya
hasil2 = saya - rekan

if rekan > saya:
    kategori = 'anda lebih ringan', int(hasil1), 'kg dari pada rekan anda'

elif saya > rekan:
    kategori = 'anda lebih berat', int(hasil2), 'kg dari rekan anda'
    
else:
    kategori = 'berat badab anda sama dengan rekan anda'
    
print('{}'.format(kategori))
