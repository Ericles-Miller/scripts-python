matriz = [0,0,0], [0,0,0], [0,0,0]
soma_t= soma_c =0
maior =0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f"Digite {j} numero da linha {i} coluna:"))

for i in range(0,3):
    soma_c += matriz[i][2]
    for j in range(0,3):
        if matriz[2][j]> maior:
            maior= matriz[2][j]
        soma_t+= matriz[i][j]

print(soma_c)
print(soma_t)
print(maior)