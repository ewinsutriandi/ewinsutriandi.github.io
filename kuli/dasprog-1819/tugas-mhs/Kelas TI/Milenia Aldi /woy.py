aldi = input('Masukan berat badan anda (kg)')
love = input('Masukan berat badan rekan anda (kg)')
love = int(love)
aldi = int(aldi)
hasil1 = love - aldi
hasil2 = aldi - love

if love > aldi:
	kategori = 'Anda lebih ringan',int (hasil1),'kg dari pada rekan anda'

elif aldi > love:
	kategori = 'Anda lebih berat',int (hasil2),'kg dari pada rekan anda'

else:
	kategori = 'Berat badan anda sama dengan rekan anda'

print ('{}'.format(kategori))
