nama = input('Nama Kamu Siapa: ')
dia = input('Nama Dia Siapa: ')
berat_ku = int(input('Masukan Berat Badan {}: kg'.format(nama)))
berat_mu = int(input('Masukan Berat Badan {}: kg'.format(dia)))
st = 'kg'
kg1 = berat_ku - berat_mu
kg2 = berat_mu - berat_ku
if berat_ku < berat_mu :
    hasil = '{} Lebih ringan {}kg dari {}'.format(nama,kg2,dia)
elif berat_ku > berat_mu :
    hasil = '{} Lebih Berat {}kg dari {}'.format(nama,kg1,dia)
else :
     hasil = '{} Berat Kamu sama dengan {}'.format(nama,dia)

print(hasil)
