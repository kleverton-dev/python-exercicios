
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

#6. Complete a tabela abaixo com os valores resultantes de avaliação do operador
#AND para cada uma das combinações de valores dados:
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#7. Agora, faça um programa em Python, que mostra o resultado do AND na tela
#para todas as combinações de valores vistas na questão anterior. A impressão
#será no formato: “O resultado da operação True and True é “ e o valor da
#resposta.
op1 = False and False
op2 = False and True
op3 = True and False
op4 = True and True
print(f"O resultado da operação False and False é {op1}")
print(f"O resultado da operação False and True é {op2}")
print(f"O resultado da operação True and False é {op3}")
print(f"O resultado da operação True and True é {op4}")

#8. Em que ordem a expressão w = x * y < z / x or x / y > z * x and z * y < x seria
#avaliada pelo Python? Descreva com detalhes essa ordem, justificando sua
#resposta.
#A ordem de avaliação da expressão é a seguinte:
#1. Parênteses: Não há parênteses na expressão, então passamos para o próximo passo.
#2. Operadores de multiplicação e divisão: x * y, z / x, x / y, z * x, z * y são avaliados primeiro.
#3. Operadores de comparação: x * y < z / x, x / y > z * x, z * y < x são avaliados em seguida.
#4. Operadores lógicos: and é avaliado antes de or, então z * x and z * y < x
#5. Finalmente, or é avaliado por último, combinando os resultados das comparações anteriores.

#9. Agora, faça um programa que receba os valores de x, y e z do usuário e mostre
#o resultado da expressão da questão anterior.
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))
resultado = x * y < z / x or x / y > z * x and z * y < x
print(f"O resultado da expressão é {resultado}")

#10. Crie um algoritmo que receba um número no formato CDU e imprima-o invertido:
#UDC. (Exemplo: 123, sairá 321.) O número deverá ser armazenado em outra
#variável antes de ser impresso.
numeros = input("Digite números de 0-9 para serem invertidos: ")
numeros_invertidos = numeros[::-1]
print(f"O número invertido é {numeros_invertidos}")

#11. Crie um algoritmo em Python que solicite um número ao usuário e informe se o
#anúmero é múltiplo de 7 (para isso, basta imprimir True ou False). Por exemplo,
#se o usuário informar o número 49, o programa deve exibir a mensagem: “49 é
#múltiplo de 7? True”.
numero = int(input("Digite um número para verificar se é múltiplo de 7: "))
print(f"{numero} é múltiplo de 7? {numero % 7 == 0}")

#12. Crie um algoritmo em Python que solicite ao usuário três nomes e informe se
#dois desses nomes são iguais, e também se todos os nomes são diferentes.

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
dois_iguais = (nome1 == nome2) or (nome1 == nome3) or (nome2 == nome3)
todos_diferentes = (nome1 != nome2) and (nome1 != nome3) and (nome2 != nome3)
print(f"Dois nomes são iguais? {dois_iguais}")
print(f"Todos os nomes são diferentes? {todos_diferentes}")

#13. Crie um algoritmo em Python que solicite ao usuário um número e informe se o
#número está dentro do intervalo entre 50 e 100. O número 50 deve ser
#considerado dentro desse intervalo, e o 100 fora do intervalo.
numero = float(input("Digite um número para verificar se está entre 50 e 100: "))
dentro_intervalo = (numero >= 50) and (numero < 100)
print(f"O número {numero} está dentro do intervalo entre 50 e 100? {dentro_intervalo}")