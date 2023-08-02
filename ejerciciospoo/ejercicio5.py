def grados(temp_F):
    temp_C = round((temp_F - 32) * 5/9, 2 )
    print("Grados Centígrados: ", temp_C,"°C")

grados(45)