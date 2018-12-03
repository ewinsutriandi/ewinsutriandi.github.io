saya = input('Masukan berat badan anda (kg)')
teman = input('Masukan berat badan teman (kg)')
teman = int(teman)
saya = int(saya)
hasil1 = teman - saya
hasil2 = saya - teman

if teman > saya:
	kategori = 'Anda lebih ringan',abs (hasil1),'kg dari pada teman'

elif saya > teman:
	kategori = 'Anda lebih berat',abs (hasil2),'kg dari pada teman'

else:
	kategori = 'Berat badan anda sama dengan teman'

print ('{}'.format(kategori))