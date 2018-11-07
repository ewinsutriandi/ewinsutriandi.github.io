berat saya = input('Masukan berat badan anda? (kg) ')
bearat rekan = input('Masukan berat badan rekan anda? (kg) ')
bearat rekan = int(bearat rekan)
berat saya = int(berat saya)
hasil1 = bearat rekan - berat saya
hasil2 = berat saya - bearat rekan

if bearat rekan > berat saya:
	kategori = 'Anda lebih ringan', int (hasil1), 'kg dari pada rekan anda'

elif berat saya > bearat rekan:
	kategori = 'Anda lebih berat',int (hasil2),'kg dari pada rekan anda'

else:
	kategori = 'Anda dan rekan anda memiliki berat badan yang sama'

print ('{}'.format(kategori))
