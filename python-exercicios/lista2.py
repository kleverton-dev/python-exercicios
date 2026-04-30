
#1. Faça um programa que solicite ao usuário dois números e mostre todos os
#resultados de possíveis de operações relacionais entre eles, ou seja, deve
#mostrar todos os resultados das operações iniciando com um número e depois
#com outro.
num1 = 10
num2 = 5

print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

#2. Faça um programa que faça o mesmo que o programa anterior, mas agora
#solicitando Strings ao usuário.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

#3. Para vários tributos, a base de cálculo é o salário-mínimo. Faça um algoritmo em
#Python que leia o valor do salário-mínimo e o valor do salário de uma pessoa.
#Em seguida, o programa deve calcular e imprimir quantos salários-mínimos a
#pessoa ganha.
salario_min = float(input("Digite o valor do salário-mínimo: "))
salario_usuario = float(input("Digite o valor do seu salário: "))
quant_salario = salario_usuario / salario_min 

print(f"Você recebe {quant_salario:.2f} salarios-mínimos.")

#4. Crie um algoritmo em Python que leia o peso de uma pessoa (em kg) e, em
#seguida, calcule e imprima o peso da pessoa em gramas e o novo peso (também
#em gramas) se a pessoa aumentar seu peso em 12%.
peso_usuario = float(input("Digite o seu peso em Kg: "))
peso_em_gramas = peso_usuario * 1000

print(f"O seu peso em gramas é {peso_em_gramas:.2f}g e seu novo peso com aumento de 12% é {peso_em_gramas * 1.12:.2f}g")

#5. Crie um algoritmo em Python para calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se
# que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade média.
tempo_gasto = float(input("Digite o tempo gasto durante a viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
distancia = tempo_gasto * velocidade_media
litros_usados = distancia / 12

print (f"O tempo gasto na viagem foi {tempo_gasto:.2f} horas.\nA velocidade média foi {velocidade_media:.2f} km/h.\nA distância percorrida foi {distancia:.2f} km.\nOs litros usados foram {litros_usados:.2f} litros.")

