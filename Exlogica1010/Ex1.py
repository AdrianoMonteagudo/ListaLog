lista_temperaturas = []
escolha = str(input("Digite a escala de origem - C para celsius e F para fahrenheit"))
def conversao(lista_temperaturas, escolha):
    lista_conversao = []
    for x in lista_temperaturas:
        if escolha == "C":
            f = x * 9/5 +32 
            lista_conversao.append(f)
        elif escolha == "F":
            c = (x -32)*5/9
            lista_conversao.append[c]
        else:
            print("Tente novamente")
    return lista_conversao

while True:
    x = float(input("Digite uma temperatura"))
    lista_temperaturas.append(x)
    parar = str(input("Deseja adicionar temperaturas? - n para não e s para sim \n"))
    if parar == "n":
        break
    elif parar == "s":
        continue
    else:
        print("Tente novamente")

print(conversao(lista_temperaturas, escolha))


    
