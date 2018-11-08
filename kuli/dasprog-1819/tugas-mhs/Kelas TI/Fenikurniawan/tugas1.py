#Feni kurniawan
#Tehnik informatika

saya = input('Masukan berat badan anda (kg)')
teman = input('Masukan berat badan teman anda (kg)')
teman = int(teman)
saya = int(saya)
hasila = teman - saya
hasilb = saya - teman
if teman > saya:
	kategori = 'Anda lebih ringan',int (hasila),'kg dari pada teman anda'

elif saya > teman:
	kategori = 'Anda lebih berat',int (hasilb),'kg dari pada teman anda'

else:
	kategori = 'Berat badan anda sama dengan teman anda'

print ('{}'.format(kategori))