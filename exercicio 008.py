medida = float(input('digite um valor em metros: '))
print(f'seu valor {medida} m, será:\n{medida*100} cm\n{medida*1000} mm')
dam = medida/10
hm = medida/100
km = medida/1000
print(f'seu valor {medida} m também será:\n{dam} dm\n{hm} hm\ne por último, será de {km} km')
