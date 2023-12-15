ite = input('berat badan anda (kg)')
amaq = input('berat badan amaq anda (kg)')
ite = int(ite)
amaq = int(amaq)
hasil1 = ite - amaq
hasil2 = amaq - ite

if ite > amaq:
	kategori = 'anda lebih berat',int (hasil1),'kg dari amaq anda'

elif amaq > ite:
	kategori = 'anda lebih ringan',int(hasil2),'kg dari amaq anda'

else:
	kategori = 'berat badan anda sama dengan amaq anda'

print('{}'.format(kategori))
