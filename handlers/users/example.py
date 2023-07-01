
narx =418
f_p = 120
ustama = 0
oy = 2
foiz_b_t = int((f_p * 100) / narx)
if foiz_b_t >= 50:
    if oy == 3 or oy == 4:
        ustama = 5
    elif oy == 5 or oy == 6:
        ustama = 6
    elif oy == 7 or oy == 8:
        ustama = 7
    elif oy >= 9 and oy <= 12:
        ustama = 8


else:
    if oy == 3 or oy == 4:
        ustama = 5
    elif oy == 5 or oy == 4:
        ustama = 6
    elif oy == 7 or oy == 4:
        ustama = 7
    elif oy >= 9 or oy <= 12:
        ustama = 8

narx_qo = narx - f_p
qoldik = narx_qo * (oy * ustama+100 ) / 100
ustama = 0
# oyiga = narx_qoo / oy

# print( oyiga)
print( narx - f_p)
print( ustama)
print( narx)
print( narx_qo * (oy * ustama+100 ) / 100)
print( qoldik )
print(narx - f_p)