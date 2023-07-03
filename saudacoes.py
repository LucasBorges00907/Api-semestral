import random

def main():
    nome = input('Qual o seu nome? ')

    print(f'\nOlá {nome}, {alegrias()}')

    numero = int(input('\nDigite um número positivo para uma nova frase e negativo para encerrar. '))

    while numero > 0:
        print(alegrias())
        numero = int(input('\nDigite um número positivo para uma nova frase e negativo para encerrar. '))

    print(f'\nTchau {nome}, {alegrias()}')



def alegrias():
    with open('alegria.txt', 'r', encoding='UTF-8') as f:
        saudacoes = f.readlines()
        index = random.randint(0, len(saudacoes) - 1)
        return saudacoes[index].strip()




main()