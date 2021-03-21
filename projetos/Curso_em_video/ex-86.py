matriz = [[], [], []], [[], [], []], [[], [], []]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f"Digite {j} numero da linha {i} coluna"))

for i in range(0,3):
    for j in range(0,3):
        print(f"{matriz[i][j]} ", end='')
    print("\n")