import random 

numero_secreto = random.randint(1, 10)

acertou = False  

while not acertou:
    palpite = int(input("Adivinhe o número: "))
    
    if palpite < numero_secreto:
        print("Tente um número MAIOR.")
    elif palpite > numero_secreto:
        print("Tente um número MENOR.")
    else:
        print("Parabéns! Você acertou!")
        acertou = True