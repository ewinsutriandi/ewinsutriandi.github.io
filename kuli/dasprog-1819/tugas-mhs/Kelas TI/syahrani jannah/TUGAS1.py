syahrani = input('Masukkan berat badan anda (kg)')
teman = input('Masukkan berat badan teman anda (kg)')
syahrani = int(syahrani)
teman = int(teman)
hasil1 = syahrani - teman
hasil2 = teman - syahrani

if syahrani > teman:
	kategori = 'anda lebih berat', int(hasil1) ,'kg dari pada teman anda'

elif teman > syahrani:
	kategori = 'anda lebih ringan', int(hasil2) ,'kg dari pada teman anda'

else:
	kategori = 'berat badan anda sama dengan teman anda'

print('{}'.format(kategori))
