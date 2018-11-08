saya = input( 'masukkan berat badan anda (kg)' )
rekan = input( 'masukkan berat badan rekan anda (kg)' )
rekan = int( rekan )
saya = int( saya )
hasil1 = rekan-saya
hasil2 = saya-rekan
if rekan > saya:
      kategori = 'kamu lebih berat' ,abs(hasil1), 'kg dari teman kamu'
elif rekan > saya:
      kategori = 'kamu lebih ringan' ,abs(hasil2), 'kg dari teman kamu'
else:
      kategori = 'berat kamu sama dengan rekan kamu '
print( '{}'.format(kategori)