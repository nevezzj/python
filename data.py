from datetime import date 
import math
p = 1
AnoNascimento = int(input('Digite o ano de Nascimento:'))
MesNascimento = int(input('Digite o mês do Nascimento:'))
DiaNascimento = int(input('Digite o dia do Nascimento:'))

diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
print(f'{diaAtual}/{mesAtual}/{anoAtual}')
r = anoAtual - AnoNascimento

if(MesNascimento > mesAtual):
    r = (anoAtual - AnoNascimento) - p
    print(r)
    
if(MesNascimento == mesAtual and DiaNascimento < diaAtual):
    y = anoAtual - AnoNascimento
    print(y)

if(diaAtual == DiaNascimento and mesAtual == MesNascimento):
    g = anoAtual - AnoNascimento
    print(g)

elif(diaAtual < DiaNascimento and mesAtual == MesNascimento):
    u = anoAtual - AnoNascimento - p
    print(u)
    
else:
    h = anoAtual - AnoNascimento
    print(h)