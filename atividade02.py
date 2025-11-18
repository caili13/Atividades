par = 0 
impar = 0

for numero in range(1,21):
    if numero % 2 == 0:
        par +=1
        
    else:
        impar += 1

print("Quantidade de numeros pares:", par)  
print("Quantidade de numeros impares:", impar)  