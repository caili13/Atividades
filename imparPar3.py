par = 0 
impar = 0

numero = int(input("Digite o número: "))

if numero % 2 == 0:
    par += 1
    print("O número é par.")
else:
    impar += 1
    print("O número é ímpar.")