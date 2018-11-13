aku = input( 'masukkan berat badan kamu:' )
sahabat = input( 'masukkan berat badan sahabatmu:' )
aku = int(aku)
sahabat = int(sahabat)
hasil1 = (aku-sahabat)
hasil2 = (sahabat-aku)

if sahabat > aku:
      kategori = 'kamu lebih ringan' ,abs(hasil1), 'kg dari sahabatmu'
elif sahabat < aku:
      kategori = 'kamu lebih berat' ,abs(hasil2), 'kg dari sahabatmu'
else:
      kategori = 'berat kamu sama dengan berat sahabatmu'
print('{}'.format(kategori))