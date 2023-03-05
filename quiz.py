print ("Seja bem vindo ao Quiz!")
answer_user = input ("Podemos iniciar? (s/n)")

if answer_user != "s": 
    quit()
score = 0
print("Vamos lá...")
print("Quanto é 4x7? \n (A) 70 \n (B) 28 \n (C) 21 \n (D) 29 \n")
answer_1 = input("Resposta: ")
if answer_1 == ("B"):
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print("Quanto é 70x7? \n (A) 528 \n (B) 470 \n (C) 490 \n (D) 500 \n")
answer_2 = input("Resposta: ")
if answer_2 == ("C"):
    print("Correto")
    score = score + 1
else:
    print("Incorreto")


print("Qual o valor de pi? \n (A) 3,14159265358979323846 \n (B) 3,1159265358979323846 \n (C) 3,24159265358979323846 \n (D) 3 \n")
answer_3 = input("Resposta: ")
if answer_3 == ("A"):
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print("Aproximadamente, quantos bits possuem em um megabyte? \n (A) 8.388.608 \n (B) 1.048.576  \n (C) 3.241.592.653 \n (D) 8 \n")
answer_4 = input("Resposta: ")
if answer_4 == ("A"):
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print("Marque a alternativa que possui pelo menos duas linguagem de marcação: \n (A) Javacript, Python e Ruby \n (B) C#, C++ e Java \n (C) HTML, CSS e XML \n (D) Electron, React e TypeScript")
answer_5 = input("Resposta: ")
if answer_5 == ("C"):
    print ("Correto")
    score = score + 1
else:
    print("Incorreto")




    
print(f"FIM... \nPontuação: {score}/5 " )