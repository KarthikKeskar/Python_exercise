starttrip=7440
endtrip=8000
Tankcapacity=10
#15kms per litre
mileage=15
#fuel consumed
print (((endtrip-starttrip)/mileage), "Litres")
stops=round(((endtrip-starttrip)/mileage)/Tankcapacity)
print (stops)



