saya = input( 'masukkan berat badan anda' )
kamu = input( 'masukkan berat badan teman' )
saya = int(saya)
kamu = int(kamu)
hasil1 = (saya- kamu)
hasil2 = (kamu-saya)
if kamu > saya:
      kategori = 'kamu lebih ringan' ,abs(hasil1), 'kg dari teman kamu'
elif kamu < saya:
      kategori = 'kamu lebih berat' ,abs(hasil2), 'kg dari teman kamu'
else:
      kategori = 'berat kamu sama dengan teman kamu '
print('{}'.format(kategori))