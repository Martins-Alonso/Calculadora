#Calculadora Simples

#Primeiro Nuḿero:
#Segunda Núnmero:
#Resultado:
#Operação: ' '

num1= int(input('Digite o primeiro número:'))

op=input('Digite a operação:')

num2= int(input('Digite o segundo número:'))

if op == '+' :
    Resultado = num1 + num2

elif op == '-' :
    Resultado = num1 - num2

elif op == '*':

    Resultado = num1 * num2

elif op == '/':

    Resultado = num1 / num2

else:

    Resultado = ' Operação inválida'

print(num1,num2,op,Resultado)




