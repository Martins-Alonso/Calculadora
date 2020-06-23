#Calculadora simples
while True:

    numero_1 = int (input('Digite o primeiro número:'))
    operacao = input ('Digite a operaçao :')
    numero_2 = int (input('Digite o segundo número:'))

    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '/':
        resultado = numero_1 / numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    else:
        resultado =  ' algo saiu errado,digite novamente'

    print(str(numero_1) +'' + str (operacao) +'' + str (numero_2) +' = '+ str(resultado))  

    
