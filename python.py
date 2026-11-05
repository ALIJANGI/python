xh = input('enter hours:')
xr = input('enter rate:')
try :
    xh = float(xh)
    xr = float(xr)
except :
    xh = -1
    xr = -1
xp = xh * xr
if xh > 0 and xr > 0:
    print('payment is',xp)
else:
    print('enter a valid number')