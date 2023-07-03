import random
def main():

    qtd_pedras = int(input("Digite um número de pedras (até 50): "))
    while qtd_pedras>50 or qtd_pedras<1:
        print("O número não pode passar de 50")
        qtd_pedras = int(input("Digite um número de pedras (até 50): "))



    
    pedras = [random.randint(1,50) for i in range(qtd_pedras)]
    for i in range(qtd_pedras):
        volume_pedra = pedras[i]
        print (volume_pedra)
    
    print(pedras)

    volume_total_chuva = reduzir(pedras, lambda x,y: x+y, 0)


    pedra_minima = calcular_pedra_minima(pedras)
    pedra_maxima = calcular_pedra_maxima(pedras)

    qtd_pedras_minimas = contar_pedras_minimas(pedras,pedra_minima)
    qtd_pedras_maximas = contar_pedras_maximas(pedras,pedra_maxima)

    volume_pedras_minimas = qtd_pedras_minimas*pedra_minima
    volume_pedras_maximas = qtd_pedras_maximas*pedra_maxima

    percentual_pedras_minimas_do_total = (volume_pedras_minimas/volume_total_chuva)*100
    percentual_pedras_maximas_do_total = (volume_pedras_maximas/volume_total_chuva)*100

    print(f"O volume total da chuva foi de {volume_total_chuva:.2f} ml")
    print(f"{qtd_pedras_minimas} saraivas tem o volume mínimo de {pedra_minima} ml")
    print(f"A soma dos volumes das saraivas com volume mínimo é de {volume_pedras_minimas:.2f} ml")
    print(f"As saraivas com volume mínimo, representam percentualmente {percentual_pedras_minimas_do_total:.2f}% do volume total de chuva")
    print('---------------------------')

    
    print(f"{qtd_pedras_maximas} saraivas tem o volume máximo de {pedra_maxima} ml")
    print(f"A soma dos volumes das saraivas com volume máximo é de {volume_pedras_maximas:.1f}")
    print(f"As saraivas com volume máximo, representam percentualmente {percentual_pedras_maximas_do_total:.1f}% do volume total de chuva")
    
    pedras_com_volume_primo = verificar_pedras_com_volume_primo(pedras)

    if pedras_com_volume_primo == []:
        print("Não existe nenhuma pedra com o volume primo")
    else:
        for item in pedras_com_volume_primo:
            print (f"Pedra com volume primo: {item} ")


    soma_multiplas_de_m = soma_pedras_multiplas_de_m(pedras)
    soma_index_par = soma_pedras_index_par(pedras)

    diferenca =  soma_index_par-soma_multiplas_de_m
    print(f"A diferença entre a soma das pedras com index pax e as pedras volumes múltiplos de M   é de {diferenca}")
    

    tamanho = len(pedras)
    volume_medio =calcular_volue_medio(volume_total_chuva,tamanho)

    ## não deu de finalizar a g :((((




def calcular_volue_medio(volume_total,tamanho):
    volume_medio = volume_total/tamanho
    return tamanho
    
def verificar_pedras_com_volume_primo(pedras):
    pedras_com_volume_primo = []
    for pedra in pedras:
        if eh_primo(pedra):
            pedras_com_volume_primo.append(pedra)
    return pedras_com_volume_primo

def verificar_pedras_com_volume_primo(pedras):
    pedras_com_volume_primo = []
    for pedra in pedras:
        if eh_primo(pedra):
            pedras_com_volume_primo.append(pedra)
    return pedras_com_volume_primo

def eh_primo(numero):
    for i in range(2,numero):
        if numero%i == 0:
            return False
    return True


def soma_pedras_multiplas_de_m(pedras):
    soma = 0
    m = int(input("Digite um número para verificar a soma de seus múltiplos: "))
    for i in pedras:
        if pedras[i]%m == 0:
            soma = soma + pedras[i]
    return soma

def soma_pedras_multiplas_de_m(pedras):
    soma = 0
    m = int(input("Digite um número (M) para verificar a soma de seus múltiplos: "))
    for i in pedras:
        if i % m == 0:
            soma = soma + i
    return soma





def soma_pedras_index_par(pedras):
    soma = 0
    for i in range(len(pedras)):
        if i%2 == 0:
            soma = soma + pedras[i]
    return soma



def calcular_pedra_minima(pedras):
    pedra_minima = pedras[0]
    for i in range(1,len(pedras)):
        if pedras[i] < pedra_minima:
            pedra_minima = pedras[i]
    return pedra_minima

def calcular_pedra_maxima(pedras):
    pedra_maxima = pedras[0]
    for i in range(1,len(pedras)):
        if pedras[i] > pedra_maxima:
            pedra_maxima = pedras[i]
    return pedra_maxima



    
def reduzir(lista,funcao,inicial):
    resultado = inicial
    for i in lista: 
        resultado = funcao(resultado,i)
    return resultado
    
def mapear(lista,funcao):
    for i in lista:
        return funcao(lista[i])
    
def filtrar(lista,funcao_boolean):
    for i in lista:
        if funcao_boolean(i):
            return i

    
        



def contar_pedras_minimas(pedras,pedra_minima):
    contador = 0
    for i in range(0,len(pedras)):
        if pedras[i] == pedra_minima:
            contador = contador + 1
    return contador

def contar_pedras_maximas(pedras,pedra_maxima):
    contador = 0
    for i in range(0,len(pedras)):
        if pedras[i] == pedra_maxima:
            contador = contador + 1
    return contador


def obter_numero (label = "Digite um número: "):
    numero = input(label)
    while not numero.isnumeric() or numero == '':
        print ("Valor inválido!")
        numero = input(label)
        return int(numero)
    

def obter_texto(label = "Digite uma string: "):
    texto = input(label)
    return texto


def mostrar_texto(texto):
    print(texto)



main()