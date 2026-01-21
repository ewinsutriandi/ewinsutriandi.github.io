Oku = input( 'masukkan berat badan anda' )
Ente = input( 'masukkan berat badan teman' )
Oku = int(Oku)
Ente = int(Ente)
hasil1 = Oku - Ente
hasil2 = Ente - Oku

if Ente > Oku:
      kategori = 'kamu lebih ringan' ,int(hasil2), 'kg dari teman kamu'
elif Oku > Ente:
      kategori = 'kamu lebih berat' ,int(hasil1), 'kg dari teman kamu'
else:
      kategori = 'berat kamu sama dengan teman kamu '
print('{}'.format(kategori))