nama = (input('masukkan nama anda'))  
nama2 = input('masukkan nama 2') 
saya = input('masukkan berat badan saya (kg)') 
teman = input('masukkan berat badan teman (kg)') 
saya = int(saya)
teman = int(teman)
berat_1 = saya - teman
berat_2 = teman - saya

if saya > teman:
	kategori = ('{} lebih berat {}kg dari {}' .format( nama, berat_1, nama2))

elif saya < teman:
	kategori = ('{} lebih ringan {}kg dari {}'  .format( nama, berat_2, nama2))

else:
	kategori = ('berat {} sama dengan teman {}'  .format( nama, nama2))

print ('{}' .format(kategori))