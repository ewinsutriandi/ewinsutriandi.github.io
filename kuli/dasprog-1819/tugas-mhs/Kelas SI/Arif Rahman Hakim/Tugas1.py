Saya = input('Masukkan berat badan rekan anda {kg}')
Rekan = input('Masukkan berat badan rekan anda {kg}')
Rekan = int(Rekan)
Saya = int(Saya)
Hasil1 = Rekan - Saya
Hasil2 = Saya - Rekan

if Rekan > Saya:
       kategori = 'Anda lebih ringan', int(Hasil1),'kg dari pada rekan anda'
			 
elif Saya > Rekan:
       kategori = 'Anda lebih berat', int(Hasil2),'kg dari rekan anda'
			 
else:
       kategori = 'Berat badan anda sama dengan rekan anda'
			 
print('{}'.format (kategori))
