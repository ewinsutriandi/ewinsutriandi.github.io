saya = input('Masukan Berat Badan Anda: (kg)')
rekan = input('masukan berat badan rekan: (kg)')
saya = int(saya)
rekan = int(rekan)
hasil1 =(saya- rekan)
hasil2 =(rekan- saya)
if saya > rekan:
       kategori = 'kamu lebih berat' ,abs(hasil1), 'kg dari rekan kamu'

elif rekan > saya:
       kategori = 'kamu lebih ringan' ,abs(hasil2), 'kg dari rekan kamu'
else:
       kategori = 'berat kamu sama dengan rekan kamu'
print('{}' .format(kategori))
