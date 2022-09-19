from random import randint
from time import sleep

print("-=-"*10)
print("[0] Pedra \n[1] Papel \n[2] Tesoura")
print("-=-"*10)
nome = str(input("Digite seu nome: ")).capitalize()
nomepc = "Computador"
user = 0
cpu = 0
v = 0
pc = 0
qtde = int(input("Você quer jogar melhor quantas? "))

for c in range(0, qtde):
    user = int(input("Digite o número da sua opção: "))
    pc = randint(0, 2)
    if user == 0:
        if pc == 0:
            print("===" * 10)
            print("{} jogou Pedra e {} jogou Pedra".format(nome, nomepc))
            print("Empate!")
            print("===" * 10)
            
        elif pc == 1:
            print("===" * 10)
            print("{} jogou Pedra e {} jogou Papel".format(nome, nomepc))
            print("{} ganhou".format(nomepc))
            print("===" * 10)
            cpu += 1
            
        elif pc == 2:
            print("===" * 10)
            print("{} jogou Pedra e {} jogou Tesoura".format(nome, nomepc))
            print("{} ganhou!".format(nome))
            v += 1
            print("===" * 10)
    sleep(0.5)
    
    if user == 1:
        if pc == 0:
            print("---" * 10)
            print("{} jogou Papel e {} jogou Pedra".format(nome, nomepc))
            print("{} venceu!".format(nome))
            v += 1
            print("---" * 10)
        elif pc == 1:
            print("---" * 10)
            print("{} jogou Papel e {} jogou Papel".format(nome, nomepc))
            print("Empate")
            print("---" * 10)
        elif pc == 2:
            print("---" * 10)
            print("{} jogou Papel e {} jogou Tesoura".format(nome, nomepc))
            print("{} ganhou".format(nomepc))
            cpu += 1
            print("---" * 10)
    sleep(0.5)
    
    if user == 2:
        if pc == 0:
            print("xxx" * 10)
            print("{} jogou Tesoura e {} jogou Pedra".format(nome, nomepc))
            print("{} ganhou".format(nomepc))
            cpu += 1
            print("xxx" * 10)
            
        elif pc == 1:
            print("xxx" * 10)
            print("{} jogou Tesoura e {} jogou Papel".format(nome, nomepc))
            print("{} ganhou! ".format(nome))
            v += 1
            print("xxx" * 10)
        elif pc == 2:
            print("xxx" * 10)
            print("{} jogou Tesoura e {} jogou Tesoura".format(nome, nomepc))
            print("Empate!")
            print("xxx" * 10)
    sleep(0.5)
    
if v == 3:
    print("Vitória perfeita!")
elif cpu == 3:
    print("Você falhou miseravelmente")

if cpu >= v:
    print("O computador ganhou com {} partidas ganha(s)".format(cpu))
elif cpu <= v:
    print("Você ganhou com {} partidas ganha(s)".format(v))
elif v == cpu:
    print("Empate em número de partidas ganha(s)")
