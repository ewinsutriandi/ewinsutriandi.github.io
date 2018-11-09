berat_saya = int(input("berat saya (kg) : "))
berat_dia = int(input("berat dia (kg) : "))
berat = berat_saya - berat_dia

if(berat_saya < berat_dia):
	print("saya lebih ringan{},kg dari dia".format(berat))
elif(berat_saya > berat_dia):
	print("saya lebih berat{},kg dari dia".format(berat))
else:
	print("berat saya sama dengan dia")
