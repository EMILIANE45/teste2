#ex 1 WHILE com contador:
'''n = int(input())
contador = 0
while contador <=n:
    if contador%2!=0:
        print(contador)
    contador += 1'''

#ex 2    
'''n = int(input())
contador = 0
while contador <=n:
    if contador%2==0:
        print(contador)
    contador += 1'''

#ex3
'''n1 = int(input())
n2 = int(input())
while n1!=n2:
    if n1 > n2:'''


#ex4
'''n= int(input())
linhas = n
rep = n
while rep!=0:
    print(linhas*"*")
    rep -=1'''


#ex5
'''n1 = int(input))
n2 = int(input))
n3 = int(input))'''

#ex6 MAIUSCULAS:
'''n = 90
cont = 65
while cont <= n:
    print(chr(cont))
    cont+=1

#MINUSCULAS:
n = 122
cont = 97
while cont <= n:
    print(chr(cont))
    cont+=1'''

#ex7
'''n = int(input())
while n!=0:
    conta=n*n
    print(conta)
    n = int(input())
    if n==0: break'''

#ex8
'''idade=int(input())
soma = 0
rep = 0
while idade!=0:
    soma = soma+idade
    idade = int(input())
    rep +=1
media = soma/rep
print(media)'''


#ex9
consult=input()
saldoI=0
while True:
    if consult=="c":
        d=float(input())
        saldoI = saldoI+d
    elif consult=="b":
        s=float(input())
        saldoI = saldoI-s
    elif consult=='a':
        print(saldoI)
    elif consult=="d":
        break
    consult=input()
print('Volte sempre!')

#ex extra
'''print('Escolha uma das opções abaixo: 1- Fazer uma soma // 2- Dizer uma frase de apoio // 3 - Sair')
e = int(input())
while e!=0:
    if e==1:
        s1=int(input('numero1'))
        s2=int(input('numero2'))
        somaT=s1+s2
        print('a soma é essa:',somaT)
        e=int(input())
    elif e==2:
        print('Tenha calma! Estamos contigo! Você consegue!')
        e=int(input())
    elif e==3: break'''
