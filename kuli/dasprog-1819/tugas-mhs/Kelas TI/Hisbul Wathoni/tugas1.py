aku = input('berat badan anda (kg)')
batur =input('berat badan teman anda (kg)')
aku=int(aku)
batur=int(batur)
hasil1 =(aku- batur)
hasil2 =(batur- aku)

if aku > batur:
	kategori = 'kamu lebih berat' ,abs(hasil1), 'kg dari teman kamu'
elif batur > aku:
	kategori = 'kamu lebih ringan' ,abs(hasil2), 'kg dari teman kamu'
else:
	kategori = 'berat kamu sama dengan teman kamu'
print('{}'.format(kategori))