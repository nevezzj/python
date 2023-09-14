nome = input("Introdusa um nome: ")
import random
b=0
computador = random.randint (0,10)
utilizador = input("Quer par ou impar: ")
if utilizador == "par":
   par = utilizador
   impar = computador
elif utilizador == "impar":
   impar = utilizador
   par = computador
else:
   b=1
   print("ERRO")

if b!=1:

   numero = input ("Digite o numero: (0/10) ")
   computador = random.randint (1,10)
   print("\nComputador escolheu: ",computador)
   print(nome," escolheu: ",numero)
   total = numero + computador
   print("A Soma é: ",total)
   computador="0"
   if total%2==0:
       print("O Resultado é: Par")
       computador="par"
   else:
       print("O Resultado é: Impar")
       computador="impar"
   if utilizador == "par" and computador=="par":
       print("Ganhou o : ",nome)
   elif utilizador == "impar" and computador=="impar":
       print("Ganhou o : ",nome)
   else:
       print("Ganhou o Computador")