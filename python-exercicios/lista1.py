#1. Faça um programa que peça um número natural ao usuário e imprima o
#quadrado desse número.
num = int(input("Digite um número: "))
print(f"O quadrado de {num} é {num ** 2}")

#2. Faça um programa que peça dois números naturais ao usuário e imprima a
#divisão do primeiro # pelo segundo. Avise ao usuário que o segundo
#número não pode ser 0.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num2 == 0:
    print("O segundo número não pode ser 0.")
else:
    print(f"A divisão de {num1} por {num2} é {num1 / num2}")

#3. Escreva um programa que peça ao usuário um número natural que representa
#o lado de um quadrado e calcule seu perímetro e a sua área.
lado = int(input("Digite o lado do quadrado: "))
perimetro = 4 * lado
area = lado ** 2
print(f"O perímetro do quadrado é {perimetro} e a área é {area}")

#4. Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
#vendas oferecendo descontos. Faça um algoritmo que solicite a entrada com o
#valor de um produto e imprima o novo valor tendo em vista que o desconto foi
#de 9%.
valor = float(input("Digite o valor do produto: "))
desconto = valor * 0.09
novo_valor = valor - desconto
print(f"O novo valor do produto com desconto é {novo_valor:.2f}")

#5. Crie um algoritmo que calcule e imprima a área de um losango. Para desenvolver
#esse algoritmo, pesquise quais os dados de entrada que precisam ser solicitados
#ao usuário, e como é feito o cálculo da área do losango.
diagonal_maior = float(input("Digite a diagonal maior do losango: "))
diagonal_menor = float(input("Digite a diagonal menor do losango: "))
area_losango = (diagonal_maior * diagonal_menor) / 2
print(f"A área do losango é {area_losango:.2f}")

#6. Escreva um programa que peça ao usuário dois números naturais para as
#variáveis A e B, e efetue as trocas dos valores de forma que a variável A passe
#a possuir o valor da variável B e a variável B passe a possuir o valor da variável
#A. Apresentar os valores trocados. OBS: não é permitido apenas imprimir o valor
#trocado. Ex.: “O valor da variável A é: “ e imprimir da variável B.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
troca = A
A = B
B = troca
print(f"O valor de A é: {A}")
print(f"O valor de B é: {B}")

#7. Escreva um programa que efetue a apresentação do valor da conversão em real
#(R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar ao usuário o
#valor da cotação do dólar, e também a quantidade de dólares que ele deseja
#converter.
cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_dolar = float(input("Digite a quantidade de dólares que deseja converter: "))
valor_real = cotacao_dolar * quantidade_dolar
print(f"O valor em real é: R${valor_real:.2f}")

#8. Escreva um programa que leia uma temperatura em graus Celsius e a apresente
#convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160) / 5,
#sendo F a temperatura em Fahrenheit, e C a temperatura em Celsius.
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (9 * celsius + 160) / 5
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")

#9. Uma empresa quer dar um bônus de Natal (em dezembro, claro) para seus
#empregados que será 60% do cálculo médio do salário de trabalho.
#Considerando que todos na empresa ganhem um mesmo valor de salário,
#elabore um programa que receba a entrada do salário e imprima o valor do bônus
#de Natal e o valor a ser depositado na conta de cada empregado em dezembro.
salario = float(input("Digite o salário do empregado: "))
bonus = salario * 0.6
valor_depositado = bonus
print(f"O valor do bônus de Natal é: R${bonus:.2f}")
print(f"O valor a ser depositado na conta do empregado é: R${valor_depositado:.2f}")

#10. Crie um algoritmo que efetue o cálculo do salário líquido de um professor. Os
#dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e
#percentual de desconto do INSS.
valor_hora_aula = float(input("Digite o valor da hora aula: "))
numero_aulas = int(input("Digite o número de aulas dadas no mês: "))
percentual_inss = float(input("Digite o percentual de desconto do INSS: "))
salario_bruto = valor_hora_aula * numero_aulas
desconto_inss = salario_bruto * (percentual_inss / 100)
salario_liquido = salario_bruto - desconto_inss
print(f"O salário líquido do professor é: R${salario_liquido:.2f}")

#11. Antes do racionamento de energia ser decretado, quase ninguém falava em
#quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.
#Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
#faça um algoritmo que receba o valor do salário mínimo e a quantidade de
#quilowatts gasta por uma residência, e calcule (imprima):
#o valor em reais de cada quilowatt;
#o valor em reais a ser pago;
#o novo valor a ser pago por essa residência com um desconto de 10%.
salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts_gastos = float(input("Digite a quantidade de quilowatts gastos: "))
valor_quilowatt = salario_minimo / 7 / 100
valor_pago = valor_quilowatt * quilowatts_gastos
valor_com_desconto = valor_pago * 0.9
print(f"O valor em reais de cada quilowatt é: R${valor_quilowatt:.2f}")
print(f"O valor em reais a ser pago é: R${valor_pago:.2f}")
print(f"O novo valor a ser pago com desconto de 10% é: R${valor_com_desconto:.2f}")